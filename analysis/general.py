import streamlit as st 

from graphics.grapichs import plotagem_h1, plotagem_h2, plotagem_h3, plotagem_h4, plotagem_h5, plotagem_h6,plotagem_h7

# Display a header
def general_display(df):
      anos_disponiveis = df[df['Ano'] <= 2023]['Ano'].unique()
      
      # Cria a barra lateral para selecionar o ano, com limite até 2023
      ano = st.sidebar.selectbox("Ano para Análise", anos_disponiveis)
      ano_filtrado = df[df['Ano'] == ano]
      
      # 1 - Evolução Mensal do Risco de Fogo em Relação à Potência Radiativa de Fogo (FRP)
      st.header(' Qual bioma apresenta maior risco de fogo no Maranhão?')     
      fig_h2 = plotagem_h2(ano_filtrado)
      if fig_h2:
            st.plotly_chart(fig_h2)
      else:
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 2 
      st.header('O aumento dos dias sem chuva está associado ao aumento do risco de fogo nos municípios mais afetados?')
      fig_h7 = plotagem_h7(ano_filtrado)
      if fig_h7:
            st.plotly_chart(fig_h7)
      else: 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 3
      st.header('Como a intensidade das queimadas varia ao longo do ano nos diferentes biomas do Maranhão?')
      fig_h3 = plotagem_h3(ano_filtrado)
      if fig_h3:
            st.plotly_chart(fig_h3)
      else : 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 4
      st.header('Existe uma correlação entre o risco de fogo e a intensidade das queimadas ao longo do ano?')
      fig_h1 = plotagem_h1(ano_filtrado)
      if fig_h1:
            st.plotly_chart(fig_h1)
      else:
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 5
      st.header('O aumento nos dias sem chuva está diretamente associado ao aumento no risco de fogo?')
      fig_out = plotagem_h4(ano_filtrado)
      if fig_out:
            st.plotly_chart(fig_out)
      else : 
            st.write("Gráfico não disponível para o ano selecionado.")
      
      # 6
      st.header('Existe uma correlação negativa entre precipitação e risco de fogo?')
      fig_h5 = plotagem_h5(ano_filtrado)
      if fig_h5:
            st.plotly_chart(fig_h5)
      else: 
            st.write("Gráfico não disponível para o ano selecionado.")
            
      # 7
      st.header('Quais municípios apresentam os maiores valores de FRP e, portanto, as queimadas mais intensas?')
      fig_h6 = plotagem_h6(ano_filtrado)
      if fig_h6:
            st.plotly_chart(fig_h6)
      else: 
            st.write("Gráfico não disponível para o ano selecionado.")
      
