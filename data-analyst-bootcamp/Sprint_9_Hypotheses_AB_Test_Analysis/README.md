# README do Projeto 9 — Priorização de Hipóteses e Análise de Teste A/B

## Introdução

Neste projeto, você atuará como analista de dados em uma grande loja online, colaborando com o departamento de marketing para priorizar hipóteses que possam aumentar a receita. Após definir a prioridade das hipóteses usando os frameworks ICE e RICE, você conduzirá a análise de um teste A/B para validar mudanças propostas e identificar qual grupo apresenta melhor performance.

## Descrição dos Dados

- **Hypotheses:** arquivo contendo 9 hipóteses para aumentar a receita, com colunas Reach, Impact, Confidence e Effort, todas em escala de 1 a 10.
- **Orders:** dados de pedidos realizados, contendo transactionId, visitorId, date, revenue e grupo (A ou B) do teste A/B.
- **Visits:** dados de visitas ao site por grupo e data.

## Objetivos

### Parte 1: Priorização de Hipóteses
- Aplicar o framework ICE para priorizar as hipóteses.
- Aplicar o framework RICE para priorizar as hipóteses.
- Comparar as diferenças nas priorizações e explicar as mudanças.

### Parte 2: Análise do Teste A/B
- Visualizar e analisar a receita acumulada por grupo.
- Analisar o tamanho médio acumulado dos pedidos.
- Calcular e plotar a taxa de conversão diária por grupo.
- Identificar e remover outliers com base nos percentis 95 e 99.
- Realizar testes estatísticos para verificar significância das diferenças entre grupos.
- Tomar decisão sobre a continuação ou finalização do teste com base nos resultados.

## Conclusão geral do projeto

Conclusões:
- As hipóteses com maior alcance (Reach) mudaram bastante entre ICE e RICE, mostrando a importância de considerar esse fator.
- O grupo B mostrou vantagem inicial na receita, mas perdeu consistência ao longo do tempo.
- O ticket médio do grupo B teve maior variabilidade e presença de outliers, o que afetou os resultados.
- A conversão foi levemente superior no grupo B, mas sem significância estatística consistente.
- Após filtrar os outliers, os resultados se tornaram mais equilibrados e indicam ausência de diferenças significativas.

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/gschmidel19/Sprint_9_Hypotheses_AB_Test_Analysis.git

2. Instale as dependências: 
pip install -r requirements.txt

3. Execute o notebook Jupyter para seguir toda análise e conclusões
jupyter notebook notebooks/sprint_9_analysis.ipynb

## Estrutura do projeto
Sprint_9_Hypotheses_AB_Test_Analysis/
├── data/
│   ├── hypotheses_us.csv
│   ├── orders_us.csv
│   └── visits_us.csv
├── notebooks/
│   └── sprint_9_analysis.ipynb
├── README.md
└── requirements.txt

