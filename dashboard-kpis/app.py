import streamlit as st
from src.load_data import carregar_dados
from src.cleaning import tratar_dados
from src.metrics import calcular_kpis

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("Dashboard de KPIs")

# carregar
df = carregar_dados()

# tratar
df = tratar_dados(df)



st.dataframe(df)