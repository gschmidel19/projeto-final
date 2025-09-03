# Projeto Sprint 8 — Y.Afisha: Otimização de Marketing com Análise de Produto e Vendas

Análise do comportamento de usuários, performance de vendas e eficiência de marketing para a empresa **Y.Afisha**, com o objetivo de otimizar os gastos em aquisição de clientes. Utilizando dados de sessões, pedidos e custos, foi possível avaliar o funil de conversão, o valor gerado por cliente (LTV) e o retorno sobre o investimento (ROI).

---

## 🧠 Introdução

Você se saiu muito bem no curso da TripleTen e recebeu uma oferta de estágio no departamento analítico da Y.Afisha. Sua primeira tarefa é ajudar a empresa a otimizar suas despesas com marketing.

Você tem:

* Logs do servidor com dados sobre os acessos a Y.Afisha (jan/2017 a dez/2018)
* Arquivo com todos os pedidos realizados
* Estatísticas de despesas com marketing

Você vai analisar:

* Como as pessoas usam o produto
* Quando começam a comprar
* Quanto dinheiro cada cliente traz para a empresa (LTV)
* Quando as despesas serão cobertas (ROI)

---

## 📊 Tecnologias e bibliotecas aplicadas

* **Linguagem:** Python
* **Ferramentas:** Jupyter Notebook, Git, GitHub
* **Bibliotecas:**

  * `pandas` — manipulação de dados
  * `numpy` — cálculos numéricos
  * `matplotlib`, `seaborn` — visualizações
  * `scipy.stats` — testes estatísticos
  * `datetime` — manipulação de datas

---

## 🔬 Práticas aplicadas

* Análise de sessões e comportamento de uso
* Agrupamento por coorte de aquisição
* Cálculo de conversão diária (0d, 1d, etc.)
* Lifetime Value (LTV)
* CAC e ROI por origem de marketing
* Visualizações por origem e dispositivo

---

## 📂 Estrutura do Projeto

```
Sprint_8_YAfisha/
├── data/
│   ├── visits_log_us.csv
│   ├── orders_log_us.csv
│   └── costs_us.csv
│
├── notebooks/
│   └── sprint_8_yafisha.ipynb
│
├── results/
│   ├── ltv_plot.png
│   ├── roi_chart.png
│   └── funnel_conversion.csv
│
├── README.md
└── requirements.txt
```

---

## 🚀 Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/Sprint_8_YAfisha.git
```

2. Instale os pacotes:

```bash
pip install -r requirements.txt
```

3. Execute o notebook:

```bash
jupyter notebook notebooks/sprint_8_yafisha.ipynb
```

---

## 📦 Arquivo requirements.txt

```
pandas
numpy
matplotlib
seaborn
scipy
```

---



