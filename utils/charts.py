import plotly.express as px 
import pandas as pd

# HIPÓTESE 1
def hipotese_um(data): 
      g1 = px.line(
            data, x='Mes', 
            y='RiscoFogo', 
            color='FRP', 
            title='Evolução Mensal do Risco de Fogo em Relação à Potência Radiativa de Fogo (FRP)', 
            text='FRP'
      )
      
      g1.update_traces(textposition='top center')
      return g1

# HIPÓTESE 2
def hipotese_dois(data):
      fig = px.bar(
            data,
            x="Mes",
            y='RiscoFogo',
            color='Bioma',
            facet_col="Bioma",
            title='Comparação do Risco de Fogo Mensal por Bioma no Maranhão',
            orientation="v",
            text='RiscoFogo'
      )
      
      fig.update_traces(textposition='outside')
      return fig

# HIPÓTESE 3
def hipotese_tres(data): 
      fig = px.bar(
            data,
            x="Mes",
            y='FRP',
            color='Bioma',
            facet_col="Bioma",
            title='Distribuição Mensal da Potência Radiativa de Fogo (FRP) nos Biomas do Maranhão',
            orientation="v",
            text='FRP'
      )
      
      fig.update_traces(textposition='outside')
      return fig

# HIPÓTESE 4
def hipotese_quatro(data):
      fig = px.scatter(
            data, 
            x="Mes", 
            y="RiscoFogo", 
            color='DiaSemChuva',
            title='Impacto dos Dias Sem Chuva no Risco de Fogo Mensal',
            text="DiaSemChuva"
      )
      
      fig.update_traces(textposition= 'top center')
      return fig

# HIPÓTESE 5 (Alternativa 1)
def hipotese_cinco(data):
      fig = px.scatter(
            data, 
            x="Mes", 
            y="Precipitacao", 
            color='RiscoFogo',
            title="Influência da Precipitação Mensal no Risco de Fogo por Bioma",
            text='RiscoFogo'
      )
      
      fig.update_traces(textposition='top center')
      return fig

# HIPÓTESE 6
def hipotese_seis(data):
      fig = px.bar(
            data, 
            x="FRP", 
            y="Municipio", 
            color='RiscoFogo', 
            title='Distribuição da Potência Radiativa de Fogo (FRP) nos Municípios com Maior Risco de Fogo',
            text='FRP',
            orientation='h',
            color_continuous_scale="RdYlBu_r",
            range_color=[data['RiscoFogo'].min(), data['RiscoFogo'].max()]
      )
      fig.update_yaxes(categoryorder='total ascending')
      fig.update_traces(textposition='outside')
      return fig

# HIPÓTESE 7
def hipotese_sete(data):
      fig = px.bar(
            data, 
            x="DiaSemChuva", 
            y="Municipio", 
            color='RiscoFogo', 
            title='Relação entre Dias Sem Chuva e Risco de Fogo nos Municípios com Maior Incidência',
            text='DiaSemChuva',
            orientation='h'
      )
      fig.update_yaxes(categoryorder='total ascending')
      fig.update_traces(textposition='outside')
      return fig
