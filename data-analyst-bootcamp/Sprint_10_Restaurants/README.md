# Projeto 10 — Pesquisa de Mercado para Cafeteria Automatizada

Este projeto visa analisar o mercado de restaurantes em Los Angeles com o objetivo de fornecer insights para a abertura de uma cafeteria inovadora, que utiliza garçons robôs. A análise abrange aspectos como tipos de estabelecimentos, características de redes, número médio de assentos, concentração de restaurantes por rua e tendências para o setor.

## Objetivos

- Avaliar as condições atuais do mercado de restaurantes em LA
- Identificar o perfil ideal de estabelecimento para o modelo de negócio
- Fornecer recomendações para desenvolvimento e expansão do negócio

## Dados Utilizados

- Dataset de restaurantes em Los Angeles contendo informações sobre nome, tipo, se faz parte de rede, endereço e número de assentos.
- Arquivo: `/datasets/rest_data_us_upd.csv`

## Etapas do Projeto

1. Carregamento e preparação dos dados (tratamento de tipos, valores ausentes e duplicados).
2. Análise exploratória para identificar padrões em tipos de estabelecimentos e redes.
3. Extração e análise dos dados de endereço para identificar ruas com maior concentração.
4. Análise da distribuição do número de assentos por tipo e rua.
5. Síntese de recomendações para investidores e parceiros.

## Tecnologias e Bibliotecas

- Python  
- Jupyter Notebook  
- Pandas, NumPy  
- Matplotlib, Seaborn, Plotly  

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/gschmidel19/Sprint_10_Restaurants.git
2. Instale os requisitos
pip install -r requirements.txt

3. Execute o notebook para acompanhar a análise:
jupyter notebook notebooks/sprint_10_restaurants.ipynb


Sprint_10_Restaurants/
├── data/
│   └── rest_data_us_upd.csv          # Dataset dos restaurantes
├── notebooks/
│   └── sprint_10_restaurants.ipynb  # Notebook com toda análise e visualizações
├── imgs/
│   └── (gráficos e imagens gerados pelo notebook, se houver)
├── requirements.txt                  # Lista de dependências
├── README.md                        # Descrição do projeto (README do projeto 10)
└── README_general.md                # README geral do repositório com todos os projetos
