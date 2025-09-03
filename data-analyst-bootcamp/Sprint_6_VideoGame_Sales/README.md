# 🎮 Sprint 6: Análise de Vendas de Jogos — Ice Store

Projeto desenvolvido durante o Bootcamp de Análise de Dados da TripleTen.

Neste projeto, assumimos o papel de analista de dados na loja online **Ice**, que comercializa videogames globalmente. Nosso objetivo é identificar padrões que indiquem se um jogo pode ser um sucesso de vendas, com base em dados históricos e variáveis como plataforma, gênero, pontuações e classificações etárias.

## 🧠 Objetivo

Analisar dados históricos até 2016 para planejar campanhas publicitárias eficazes em 2017, identificando características comuns entre jogos de sucesso.

## 📁 Estrutura do Projeto

Sprint_6_VideoGame_Sales/
│
├── datasets/
│ └── games.csv # Conjunto de dados com informações de vendas
│
├── notebooks/
│ └── sprint_6_games_analysis.ipynb # Análise exploratória e estatística
│
├── README.md
├── requirements.txt
└── .gitignore


## 🔍 Etapas do Projeto

1. **Importação e preparação dos dados**  
   - Padronização de colunas  
   - Conversão de tipos  
   - Tratamento de valores ausentes  
   - Cálculo de vendas globais

2. **Análise exploratória e tendências**
   - Evolução das vendas por ano e plataforma  
   - Identificação de plataformas emergentes e obsoletas  
   - Gêneros mais vendidos e lucrativos  
   - Impacto de críticas e notas de usuários

3. **Análise regional (NA, EU, JP)**
   - Plataformas e gêneros dominantes por região  
   - Influência da classificação ESRB em cada mercado

4. **Testes de hipótese**
   - Comparação de médias entre:
     - Xbox One x PC (User Score)
     - Gêneros Action x Sports

## 📊 Tecnologias e Bibliotecas

- **Python 3.10+**
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- plotly (opcional)

## 🧪 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/gscmidel19/Sprint_6_VideoGame_Sales.git
   cd Sprint_6_VideoGame_Sales

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

pip install -r requirements.txt

jupyter notebook notebooks/sprint_6_games_analysis.ipynb

📝 Dados
O arquivo games.csv está disponível na pasta datasets/.

As colunas disponíveis:

Name, Platform, Year_of_Release, Genre, NA_sales, EU_sales, JP_sales, Other_sales, Critic_Score, User_Score, Rating