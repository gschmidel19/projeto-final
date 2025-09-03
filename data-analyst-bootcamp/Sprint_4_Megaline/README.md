# Sprint 4 - Projeto Megaline: Análise Estatística de Dados

## Descrição do Projeto

Neste projeto, você trabalha como analista de dados para a empresa de telecomunicações Megaline, que oferece dois planos pré-pagos: **Surf** e **Ultimate**.  
O objetivo é analisar o comportamento dos clientes e determinar qual dos planos gera mais receita para a empresa, a partir dos dados de 500 clientes em 2018.

---

## Objetivos

- Preparar e limpar os dados das tabelas fornecidas: usuários, chamadas, mensagens, internet e planos.  
- Calcular métricas mensais por usuário: minutos usados, mensagens enviadas, volume de dados consumidos e receita gerada.  
- Descrever o comportamento dos clientes para cada plano com estatísticas descritivas (média, variância, desvio padrão).  
- Visualizar distribuições por meio de histogramas.  
- Testar hipóteses estatísticas para comparar receitas médias entre planos e regiões.  
- Concluir qual plano é mais rentável para a empresa.

---

## Estrutura do Repositório

Sprint_4_Megaline/
│
├── data/
│ ├── megaline_calls.csv
│ ├── megaline_internet.csv
│ ├── megaline_messages.csv
│ ├── megaline_plans.csv
│ └── megaline_users.csv
│
├── notebooks/
│ └── sprint_4_megaline_analysis.ipynb
│
├── README.md
│
└── requirements.txt

---

## Tecnologias e Bibliotecas

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib / Seaborn / Plotly (para visualizações)  
- SciPy (para testes estatísticos)  

---

## Como executar

1. Clone este repositório.  
2. Instale as dependências com:  
   ```bash
   pip install -r requirements.txt

Abra o notebook em notebooks/sprint_4_megaline_analysis.ipynb.

Execute as células na ordem, analisando os dados e preenchendo as explicações.

Resultados esperados
Análise descritiva dos planos Surf e Ultimate.

Visualizações dos dados de uso e receita.

Testes de hipótese com conclusões sobre a diferença de receitas entre planos e regiões.

Autor
Gabriel Schmidel 
LinkedIn
gschmidel@hotmail.com