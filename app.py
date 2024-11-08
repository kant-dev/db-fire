import streamlit as st
from utils.load_data import read_files
from analysis.general import general_display

# Configuração inicial do Streamlit
st.set_page_config(layout='wide')

# Carregando os dados
df = read_files()

# Exibindo a análise
general_display(df)
