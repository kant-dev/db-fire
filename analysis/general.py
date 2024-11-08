import streamlit as st 

from graphics.grapichs import plotagem_h1, plotagem_h2, plotagem_h3, plotagem_h4, plotagem_h5, plotagem_h6,plotagem_h7

# Display a header
def general_display(df):
      anos_disponiveis = df[df['Ano'] <= 2023]['Ano'].unique()
      
      # Cria a barra lateral para selecionar o ano, com limite até 2023
      ano = st.sidebar.selectbox("Ano para Análise", anos_disponiveis)
      ano_filtrado = df[df['Ano'] == ano]
      
      # 4 - Evolução Mensal do Risco de Fogo em Relação à Potência Radiativa de Fogo (FRP)
      st.header('Hipotese 1')
      fig_h1 = plotagem_h1(ano_filtrado)
      if fig_h1:
            st.plotly_chart(fig_h1)
      else:
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 5 -Comparação do Risco de Fogo Mensal por Bioma no Maranhão
      st.header('Hipotese 2')     
      fig_h2 = plotagem_h2(ano_filtrado)
      if fig_h2:
            st.plotly_chart(fig_h2)
      else:
            st.write("Gráfico não disponível para o ano selecionado.")
      

      # 2 -  Influência dos Dias Sem Chuva no Risco de Fogo
      st.header('Hipotese 3')
      fig_h3 = plotagem_h3(ano_filtrado)
      if fig_h3:
            st.plotly_chart(fig_h3)
      else : 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 1 - Sazonalidade do Risco de Fogo
      st.header('Hipotese 4')
      fig_out = plotagem_h4(ano_filtrado)
      if fig_out:
            st.plotly_chart(fig_out)
      else : 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 5 - Relação entre Precipitação e Risco de Fogo
      st.header('Hipotese 5')
      fig_h5 = plotagem_h5(ano_filtrado)
      if fig_h5:
            st.plotly_chart(fig_h5)
      else: 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      st.header('Hipotese 6')
      fig_h6 = plotagem_h6(ano_filtrado)
      if fig_h6:
            st.plotly_chart(fig_h6)
      else: 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      st.header('Hipotese 7')
      fig_h7 = plotagem_h7(ano_filtrado)
      if fig_h7:
            st.plotly_chart(fig_h7)
      else: 
            st.write("Gráfico não disponível para o ano selecionado.")
      