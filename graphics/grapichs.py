import streamlit as st
from utils.charts import (
      hipotese_um, hipotese_dois, hipotese_tres, hipotese_quatro, hipotese_cinco, hipotese_seis, hipotese_sete
)
# Função para plotar o gráfico da Hipótese 1
def plotagem_h1(ano_filtrado):
      if 'RiscoFogo' in ano_filtrado.columns and 'FRP' in ano_filtrado.columns:
            mm_ano = ano_filtrado.groupby('Mes')[['RiscoFogo', 'FRP']].mean().reset_index()
            mm_ano['RiscoFogo'] = mm_ano['RiscoFogo'].map(lambda x: f'{x:.2f}')
            mm_ano['FRP'] = mm_ano['FRP'].map(lambda x: f'{x:.2f}')
            return hipotese_um(mm_ano)
      else:
            st.warning("Dados insuficientes para gerar o gráfico. A coluna 'RiscoFogo' ou 'FRP' está ausente.")
            return None

# Função para plotar o gráfico da Hipótese 2
def plotagem_h2(ano_filtrado):
      if 'RiscoFogo' in ano_filtrado.columns and 'Bioma' in ano_filtrado.columns:
            # Calcule a média apenas da coluna 'RiscoFogo', mantendo "Bioma" como rótulo
            mm_ano = ano_filtrado.groupby(['Mes', 'Bioma'])[['RiscoFogo']].mean().reset_index()
            mm_ano['RiscoFogo'] = mm_ano['RiscoFogo'].map(lambda x: f'{x:.2f}')
            
            # Criação dos gráficos para a Hipótese 2
            fig_h2_1 = hipotese_dois(mm_ano)
            
            return fig_h2_1
      else:
            st.warning("Dados insuficientes para gerar o gráfico da Hipótese 2.")
            return None, None

# Função de plotagem de um outro gragfico
def plotagem_h3(ano_filtrado):
      # Implementar aqui a plotagem do gráfico para a Hipótese 2 dois
      if 'FRP' in ano_filtrado.columns and 'Bioma' in ano_filtrado.columns:
            # Calcule a média apenas da coluna 'RiscoFogo', mantendo "Bioma" como rótulo
            mm_ano = ano_filtrado.groupby(['Mes', 'Bioma'])[['FRP']].mean().reset_index()
            mm_ano['FRP'] = mm_ano['FRP'].map(lambda x: f'{x:.2f}')
            
            # Criação dos gráficos para a Hipótese 2
            fig_h2_1 = hipotese_tres(mm_ano)
            
            return fig_h2_1
      else:
            st.warning("Dados insuficientes para gerar o gráfico da Hipótese 2.")
            return None, None

# Função para plotar o gráfico da Hipótese 3
def plotagem_h4(ano_filtrado):
      if 'DiaSemChuva' in ano_filtrado.columns and 'RiscoFogo' in ano_filtrado.columns:
            mm_ano = ano_filtrado.groupby(['Mes'])[['DiaSemChuva','RiscoFogo']].mean().reset_index()
            mm_ano['DiaSemChuva'] = mm_ano['DiaSemChuva'].map(lambda x: f'{x:.2f}')
            mm_ano['RiscoFogo'] = mm_ano['RiscoFogo'].map(lambda x: f'{x:.2f}')
            
            fig = hipotese_quatro(mm_ano)
            return fig
      else:
            st.warning("Dados insuficientes para gerar o gráfico da Hipótese 3.")
            return None

def plotagem_h5(ano_filtrado):
      mes_abrev = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
      # Implementar aqui a plotagem do gráfico para a Hipótese 5 dois
      if 'Precipitacao' in ano_filtrado.columns and 'RiscoFogo' in ano_filtrado.columns:
            mm_ano = ano_filtrado.groupby(['Mes'])[['Precipitacao','RiscoFogo']].mean().reset_index()
            #mm_ano['Mes'] = mm_ano['Mes'].map(mes_abrev)  # Mapeia números para abreviações
            mm_ano['Precipitacao'] = mm_ano['Precipitacao'].map(lambda x: f'{x:.2f}')
            mm_ano['RiscoFogo'] = mm_ano['RiscoFogo'].map(lambda x: f'{x:.2f}')
            
            fig = hipotese_cinco(mm_ano)
            return fig
      else:
            st.warning("Dados insuficientes para gerar o gráfico da Hipótese 5.")
            return None

# Função para plotar o gráfico da Hipótese 6
def plotagem_h6(ano_filtrado):
      # Verifica se as colunas necessárias estão presentes
      if 'Municipio' in ano_filtrado.columns and 'RiscoFogo' in ano_filtrado.columns and 'FRP' in ano_filtrado.columns:
            # Agrupa os dados por município e calcula a média de Precipitação e RiscoFogo
            mm_ano = ano_filtrado.groupby(['Municipio'])[['FRP', 'RiscoFogo']].mean().reset_index()

            # Seleciona os cinco municípios com maior média de RiscoFogo
            top_10_municipios = mm_ano.nlargest(11, 'RiscoFogo')

            # Formata Precipitação e RiscoFogo para duas casas decimais
            top_10_municipios['FRP'] = top_10_municipios['FRP'].map(lambda x: f'{x:.2f}')
            top_10_municipios['RiscoFogo'] = top_10_municipios['RiscoFogo'].map(lambda x: f'{x:.2f}')

            # Passa os dados dos top 5 municípios para a função de plotagem
            return hipotese_seis(top_10_municipios)
      else:
            st.warning("Dados insuficientes para gerar o gráfico da Hipótese 6.")
            return None

# Função para plotar o gráfico da Hipótese 7
def plotagem_h7(ano_filtrado):
      # Verifica se as colunas necessárias estão presentes
      if 'Municipio' in ano_filtrado.columns and 'DiaSemChuva' in ano_filtrado.columns and 'RiscoFogo' in ano_filtrado.columns:
            # Agrupa os dados por município e calcula a média de Precipitação e RiscoFogo
            mm_ano = ano_filtrado.groupby(['Municipio'])[['DiaSemChuva', 'RiscoFogo']].mean().reset_index()

            # Seleciona os cinco municípios com maior média de RiscoFogo
            top_10_municipios = mm_ano.nlargest(11, 'DiaSemChuva')

            # Formata Precipitação e RiscoFogo para duas casas decimais
            top_10_municipios['DiaSemChuva'] = top_10_municipios['DiaSemChuva'].map(lambda x: f'{x:.2f}')
            top_10_municipios['RiscoFogo'] = top_10_municipios['RiscoFogo'].map(lambda x: f'{x:.2f}')

            # Passa os dados dos top 5 municípios para a função de plotagem
            return hipotese_sete(top_10_municipios)
      else:
            st.warning("Dados insuficientes para gerar o gráfico da Hipótese 6.")
            return None