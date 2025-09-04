# =========================
# E-Commerce: Segmentação de clientes
# Streamlit Dashboard completo (versão ajustada)
# =========================

import streamlit as st
import pandas as pd
import numpy as np
import re
from datetime import datetime
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import plotly.express as px

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# =========================
# 1) Carregar dados
# =========================
@st.cache_data
def load_data(path):
    df = pd.read_csv(path, encoding='utf-8')
    df = df[df['CustomerID'].notna() & df['InvoiceDate'].notna()]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
    df['Total'] = df['Quantity'] * df['UnitPrice']
    df = df[df['Total'] > 0]
    return df

df = load_data("ecommerce_dataset_us.csv")

# =========================
# 2) Filtrar por data (Streamlit date input)
# =========================
min_date = df['InvoiceDate'].min().date()
max_date = df['InvoiceDate'].max().date()

start_date, end_date = st.sidebar.date_input(
    "Selecione período",
    [min_date, max_date]
)

df = df[
    (df['InvoiceDate'] >= pd.to_datetime(start_date)) &
    (df['InvoiceDate'] <= pd.to_datetime(end_date))
]

st.sidebar.write("📅 Período filtrado:", start_date, "→", end_date)
st.write("✅ Dados carregados:", df.shape)

# =========================
# 3) Categorias a partir da Description
# =========================
def map_category(desc: str) -> str:
    if not isinstance(desc, str):
        return 'Outros'
    d = desc.lower()
    rules = [
        ('kitchen|mug|cup|plate|bowl|spoon|fork|knife|teapot', 'Cozinha'),
        ('candle|lamp|frame|vase|cushion|rug|mirror|decor', 'Decoracao'),
        ('toy|game|puzzle|doll|train|car', 'Brinquedos'),
        ('bag|wallet|purse|tote|backpack', 'Acessorios'),
        ('bath|towel|soap|sponge', 'Banho'),
        ('garden|plant|flower|pot', 'Jardim'),
    ]
    for pat, cat in rules:
        if re.search(pat, d):
            return cat
    return 'Outros'

df['Category'] = df['Description'].apply(map_category)

# Preferências por cliente (proporção)
cat_counts = df.groupby(['CustomerID','Category'])['Quantity'].sum().reset_index()
cat_pivot = cat_counts.pivot(index='CustomerID', columns='Category', values='Quantity').fillna(0)
cat_pivot = cat_pivot.div(cat_pivot.sum(axis=1), axis=0).fillna(0)

# =========================
# 4) RFM
# =========================
max_date = df['InvoiceDate'].max()
recency = df.groupby('CustomerID')['InvoiceDate'].max().apply(lambda d: (max_date - d).days)
frequency = df.groupby('CustomerID')['InvoiceNo'].nunique()
monetary = df.groupby('CustomerID')['Total'].sum()
rfm = pd.DataFrame({'Recency': recency, 'Frequency': frequency, 'Monetary': monetary})

# =========================
# 5) Base de cluster (RFM + categorias)
# =========================
base = rfm.join(cat_pivot, how='left').fillna(0)
scaler = StandardScaler()
X = scaler.fit_transform(base)

# =========================
# 6) Clustering: Silhouette e melhor K
# =========================
sil_scores = {}
for k in range(2, 9):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X)
    sil_scores[k] = silhouette_score(X, labels)

best_k = max(sil_scores, key=sil_scores.get)
km = KMeans(n_clusters=best_k, n_init=10, random_state=42)
base['Cluster'] = km.fit_predict(X)

st.sidebar.write("**Melhor K (silhouette):**", best_k)

# =========================
# 7) Visualização clusters (PCA)
# =========================
pca = PCA(n_components=2)
coords = pca.fit_transform(X)
df_clusters = pd.DataFrame(coords, columns=['PC1','PC2'], index=base.index)
df_clusters['Cluster'] = base['Cluster'].values
df_clusters['CustomerID'] = base.index

fig = px.scatter(
    df_clusters, x='PC1', y='PC2', color='Cluster',
    hover_data=['CustomerID'], title='🎯 Clusters de clientes'
)
st.plotly_chart(fig, use_container_width=True)

# =========================
# 8) Heatmap de categorias por cluster
# =========================
cat_cluster = base.copy()
cluster_means = cat_cluster.groupby('Cluster')[cat_pivot.columns].mean()

fig_heat = px.imshow(
    cluster_means.values,
    labels=dict(x="Categoria", y="Cluster", color="Proporção"),
    x=cluster_means.columns,
    y=cluster_means.index,
    aspect="auto",
    title="🛍️ Preferências médias por categoria"
)
st.plotly_chart(fig_heat, use_container_width=True)

# =========================
# 9) Perfil dos clusters
# =========================
st.subheader("📊 Perfil dos clusters")
cluster_profile = base.groupby('Cluster').agg({
    'Recency':'median',
    'Frequency':'median',
    'Monetary':'median',
    **{c:'mean' for c in cat_pivot.columns}
}).sort_index()
st.dataframe(cluster_profile)

# =========================
# 10) Resumo por pedido
# =========================
orders = df.groupby('InvoiceNo').agg(
    CustomerID=('CustomerID','first'),
    OrderDate=('InvoiceDate','min'),
    OrderTotal=('Total','sum')
).reset_index()
orders = orders.merge(base['Cluster'], left_on='CustomerID', right_index=True, how='left')
orders_summary = orders.groupby('Cluster').agg(
    NumOrders=('InvoiceNo','count'),
    TotalRevenue=('OrderTotal','sum'),
    AvgOrder=('OrderTotal','mean')
).reset_index()
st.subheader("📦 Resumo por cluster")
st.dataframe(orders_summary)

# =========================
# 11) Testes estatísticos
# =========================
st.subheader("📈 Testes estatísticos")

# H1: AOV difere entre clusters
groups = [g['OrderTotal'].values for _, g in orders.groupby('Cluster')]
H, p = stats.kruskal(*groups)
st.write(f"H1 (Kruskal clusters AOV): H={H:.3f}, p={p:.4f}")

# H2: taxa de recompra: clientes Cozinha vs Decoração
pref = cat_pivot[['Cozinha','Decoracao']].copy()
pref['pref_group'] = np.where(pref['Cozinha'] >= pref['Decoracao'], 'Cozinha', 'Decoracao')
rf = rfm.join(pref['pref_group'])
tab = rf.assign(recompra=(rf['Frequency']>1).astype(int)).groupby('pref_group')['recompra'].agg(['sum','count'])
count = tab['sum'].values
nobs = tab['count'].values
z_stat, p2 = proportions_ztest(count, nobs)
st.write(f"H2 (recompra Cozinha vs Decoracao): z={z_stat:.3f}, p={p2:.4f}")

# H3: pedidos dias úteis vs fim de semana
orders['weekday'] = orders['OrderDate'].dt.weekday
wk = orders['OrderTotal'][orders['weekday']<5]
we = orders['OrderTotal'][orders['weekday']>=5]
tstat, p3 = stats.mannwhitneyu(wk, we, alternative='two-sided')
st.write(f"H3 (úteis vs fds, Mann-Whitney): U≈{tstat:.3f}, p={p3:.4f}")
