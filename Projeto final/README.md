# E-Commerce: Identificação de Perfis de Consumidores

## 📝 Descrição
Este projeto tem como objetivo segmentar usuários da loja online Everything Plus com base em seu histórico de compras, utilizando técnicas de **RFM**, **clustering** e análise de categorias de produtos. A segmentação permite que o time de Marketing direcione campanhas personalizadas para aumentar vendas e maximizar lucro.

## 📊 Dados
- Arquivo: `ecommerce_dataset_us.csv`
- Colunas:
  - `InvoiceNo`: identificador do pedido
  - `StockCode`: identificador do item
  - `Description`: nome do item
  - `Quantity`
  - `InvoiceDate`: data do pedido
  - `UnitPrice`: preço por item
  - `CustomerID`

## 🛠 Metodologia
1. **Limpeza de dados**
   - Remoção de devoluções (InvoiceNo iniciando com "C")
   - Filtragem de `Quantity > 0` e `UnitPrice > 0`
   - Conversão de datas e criação da coluna `Total` (Quantity × UnitPrice)

2. **Análise exploratória (EDA)**
   - Compras por dia
   - Total de compras por dia
   - Histograma de valores de pedidos
   - Produtos e categorias mais vendidos
   - Sazonalidade (dia da semana, mês)

3. **Engenharia de features**
   - Criação de categorias a partir da coluna `Description`
   - Preferência por categoria (proporção de compras)
   - Features RFM: Recency, Frequency, Monetary

4. **Segmentação (Clustering)**
   - Normalização das features
   - Escolha de K pelo silhouette score
   - K-Means clustering
   - Rotulagem interpretável dos clusters (ex.: "Alta frequência / Alto ticket – Cozinha")

5. **Testes de hipóteses**
   - Diferença do ticket médio entre clusters
   - Diferença na taxa de recompra entre clientes “Cozinha” vs “Decoração”
   - Diferença de compras entre dias úteis e finais de semana

6. **Dashboards**
   - Sugestão 1: número de compras por dia, clientes e filtro de data
   - Sugestão 2: total de compras por dia, histograma de pedidos e filtro de data
   - Implementação possível via **Streamlit** e **Plotly**

## 🎯 Objetivos de Negócio
- Identificar segmentos de clientes com maior potencial de vendas
- Maximizar receita e ticket médio através de campanhas personalizadas
- Melhorar a retenção de clientes e fidelização
- Apoiar decisões estratégicas do time de Marketing

## 📈 Resultados Esperados
- Segmentos claros de clientes com comportamento distinto
- Insights acionáveis para campanhas direcionadas
- Projeção de impacto financeiro em faturamento e ROI

## 📂 Estrutura de Arquivos
/project-root
│
├─ ecommerce_dataset_us.csv
├─ notebook.ipynb
├─ app.py # Streamlit dashboard
├─ README.md
└─ output/
└─ Ecommerce_Segmentacao_Apresentacao_Final.pdf


## 📚 Referências
- Scikit-learn (KMeans, Silhouette)
- Pandas (GroupBy, Resampling)
- Plotly Express (visualizações interativas)
- Statsmodels / SciPy (testes estatísticos)
- Streamlit (dashboards)
- Guias e artigos de RFM e segmentação em e-commerce
