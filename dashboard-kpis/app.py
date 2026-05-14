import streamlit as st
from src.load_data import carregar_dados
from src.metrics import calcular_kpis

import streamlit as st
from src.load_data import carregar_dados

# carregar dados
df_raw = carregar_dados()

