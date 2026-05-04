import streamlit as st
from src.load_data import carregar_dados
from src.cleaning import limpar_dados, criar_features
from src.metrics import calcular_kpis

import streamlit as st
from src.load_data import carregar_dados
from src.cleaning import limpar_dados

# carregar dados
df_raw = carregar_dados()

# tratar dados
df_tratado = limpar_dados(df_raw.copy())

st.title("Comparação de Dados")

st.subheader("📄 Dados Brutos")
st.dataframe(df_raw)

st.subheader("✨ Dados Tratados")
st.dataframe(df_tratado)