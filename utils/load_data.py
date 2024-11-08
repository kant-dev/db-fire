import pandas as pd

def read_files():
      csv_files = [
            'data/queimadas_2019.csv',
            'data/queimadas_2020.csv',
            'data/queimadas_2021.csv',
            'data/queimadas_2022.csv',
            'data/queimadas_2023.csv',
      ]
      
      # Lê e concatena os arquivos CSV
      data = pd.concat([pd.read_csv(file, sep=',', decimal='.') for file in csv_files], ignore_index=True)

      # Converte a coluna DataHora para datetime
      data['DataHora'] = pd.to_datetime(data['DataHora'], errors='coerce')
      
      # Cria a coluna 'Ano' e 'Mes'
      data['Ano'] = data['DataHora'].dt.year  # Extrai apenas o ano como número
      data['Mes'] = data['DataHora'].dt.strftime('%Y-%m')  # Formata o mês e o ano
      
      return data
