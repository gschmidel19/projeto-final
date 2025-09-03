import sys
import getopt
import pandas as pd
import re
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

print("Script rodando")

def parse_arguments():
    """
    Analisar argumentos da linha de comando para retornar o caminho do arquivo.
    
    Retorna:
        file_path (str): O caminho para o arquivo fornecido pelo usuário.
    """
    unixOptions = "f:"
    gnuOptions = ["file="]

    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]  # excluir o nome do script

    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    file_path = ''

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-f", "--file"):
            file_path = currentValue
    
    return file_path

def extract_year_from_path(file_path):
    # Dividir o caminho do arquivo em partes
    year = file_path.split('/')[-1].split('.')[0][-4:]
    
    return year

def data_already_exists(engine, table_name, year):
    try:
        with engine.connect() as connection:
            # Consultar a nova tabela
            query = text(f'SELECT * FROM {table_name} WHERE ANO_EGRESO={year}')
            result = connection.execute(query)
            exists = result.fetchone() is not None
    except OperationalError as e:
            exists = False
    return exists

def load_data(file_path):
    df = pd.read_csv(file_path, encoding='latin1', delimiter=';')
    return df

def preprocess_data(df, threshold=0.5):
    """
    Pré-processar o DataFrame removendo as linhas em que a maioria das colunas contêm o caractere '*'.

    Args:
        df (pd.DataFrame): O DataFrame de entrada.
        threshold (float): A proporção de colunas que podem conter '*' antes que a linha seja removida.

    Retorna:
        pd.DataFrame: O DataFrame limpo.
    """
    ## Excluir linhas vazias
    ## Calcular o número de colunas
    num_columns = df.shape[1]

    # Determinar o número de caracteres '*' permitidos com base no limite
    allowed_stars = int(num_columns * threshold)

    # Filtrar as linhas em que o número de caracteres '*' excede o limite permitido
    cleaned_df = df[df.apply(lambda x: (x == '*').sum() <= allowed_stars, axis=1)]
    
    # Formato de dados
    cleaned_df.loc[:,'COMUNA_RESIDENCIA'] = cleaned_df['COMUNA_RESIDENCIA'].astype(int)
    cleaned_df.loc[:,'REGION_RESIDENCIA'] = cleaned_df['REGION_RESIDENCIA'].astype(int)
    cleaned_df.loc[:,'ANO_EGRESO'] = cleaned_df['ANO_EGRESO'].astype(int)
    
    # Renomear as colunas
    new_column_names = ['PERTENENCIA_ESTABLECIMIENTO_SALUD', 'SEXO', 'GRUPO_EDAD', 'ETNIA',
       'GLOSA_PAIS_ORIGEN', 'COMUNA_RESIDENCIA', 'GLOSA_COMUNA_RESIDENCIA',
       'REGION_RESIDENCIA', 'GLOSA_REGION_RESIDENCIA', 'PREVISION',
       'GLOSA_PREVISION', 'ANO_EGRESO', 'DIAG1', 'DIAG2', 'DIAS_ESTADA',
       'CONDICION_EGRESO', 'INTERV_Q', 'PROCED']
    old_column_names = cleaned_df.columns
    
    column_mapping = dict(zip(old_column_names, new_column_names))
    cleaned_df.rename(columns=column_mapping, inplace=True)

    return cleaned_df

def create_db_engine(db_name):
    connection_string = f'sqlite:///{db_name}'
    engine = create_engine(connection_string)
    print(f'[INFO]: Conexão verificada: {connection_string}')
    return engine

def save_to_database(df, engine, table_name):
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    
def validate_data(engine, table_name):  
    with engine.connect() as connection:
        # Consultar a nova tabela
        query = text(f'SELECT ANO_EGRESO, count(*) FROM {table_name} GROUP BY ANO_EGRESO')
        result = connection.execute(query)

        rows = result.fetchall()
        for row in rows[:100]:
            print(row)                    
      
if __name__ == "__main__":
    print('[DEBUG]: Iniciando execução do pipeline')  # ← Adiciona aqui

    # Analisar o caminho do arquivo usando os argumentos da linha de comando
    file_path = parse_arguments()
    table_name = 'egresos_pacientes'
    
    # Carregar o banco de dados no seu sistema
    engine = create_db_engine('database/ministerio_de_salud_chile.db')   
    print('[INFO]: Conexão com o banco de dados')
    
    if file_path:    
        print(f"[INFO]: Caminho do arquivo: {file_path}")
        year = extract_year_from_path(file_path)
         
        # Carregar seu arquivo CSV em um DataFrame do Pandas      
        raw_data = load_data(file_path)
        print('[INFO]: Dados carregados no DataFrame')
        
        # Verificar se os dados já estão no banco de dados
        if data_already_exists(engine, table_name, year):
            print(f"[INFO]: Os dados de {year} já existem no banco. Nenhuma ação tomada.")    
        else:
            # Pré-processar os dados
            raw_data = preprocess_data(raw_data)
            print('[INFO]: Dados pré-processados')
            
            # Salvar os dados em uma nova tabela dentro do banco de dados existente  
            save_to_database(raw_data, engine, table_name)
            print('[INFO]: Dados carregados no banco de dados')
    else:
        print('[ERRO]: Nenhum caminho foi fornecido')
    
    validate_data(engine, table_name)
