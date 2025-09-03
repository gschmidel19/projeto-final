Projeto Sprint 7: Análise de Corridas de Taxi em Chicago - Zuber

📅 Contexto

A Zuber é uma nova empresa de compartilhamento de caronas que está sendo lançada em Chicago. Este projeto tem como objetivo analisar os dados de corridas de táxi na cidade para entender:

Preferências de passageiros
Impacto do clima na duração e frequência das viagens
Tendências nas empresas de táxi mais utilizadas e nos destinos mais populares

🔬 Objetivos do Projeto

Consulta e manipulação de dados com SQL: cruzamento de tabelas para obter insights sobre volume de viagens, clima e bairros.
Análise de dados em Python: exploração de dados com pandas, visualizações com matplotlib/seaborn.
Teste de Hipóteses: avaliar se o clima influencia a duração das viagens aos sábados entre bairros específicos.


🔍 Etapas Realizadas

SQL:

Consulta dos bairros e empresas de táxi com maior volume de viagens
Agrupamento de empresas com base no nome
Categorizacão de condições climáticas
Junção de tabelas para recuperar dados de viagens entre Loop e O'Hare


Python:

Importação dos dados exportados do banco (CSV)
Limpeza e verificação de tipos
Criação de gráficos para:
Empresas de táxi mais populares
Top 10 bairros de destino


Teste de Hipótese:

H0: A duração média das corridas aos sábados é igual em dias chuvosos e não chuvosos
H1: A duração média é diferente
Nível de significância adotado: 5%


📊 Tecnologias Usadas

Linguagens & Ferramentas:

-SQL
-Python
-Jupyter Notebook
-Bibliotecas Aplicadas:
-pandas
-numpy
-matplotlib
-seaborn
-scipy (para testes de hipótese)

⚖️ Como Executar o Projeto

1. Clone o repositório:
git clone https://github.com/gschmidel19/Sprint_7_Zuber.git

2. Instale as dependências:
pip install -r requirements.txt

3. Abra o notebook:
jupyter notebook notebooks/zuber_analysis.ipynb

✅ Conclusões Gerais

1. Flash Cab e Taxi Affiliation Services lideram em volume de corridas.
2. O clima tem um impacto sutil, mas identificável, na duração das viagens entre bairros.
3. Os destinos mais frequentes ajudam a entender a logística urbana e demanda.








