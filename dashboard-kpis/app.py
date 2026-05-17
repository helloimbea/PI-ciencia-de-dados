import streamlit as st
from src.load_data import (
    load_cargos,
    load_linguagens,
    load_faixa_salarial,
    load_ia_salario,
    load_nivel_salario,
)
from src.metrics import (
    calcular_media_salarial,
    calcular_tecnologia_principal,
    calcular_amostra,
    grafico_cargos,
    grafico_linguagens,
    grafico_faixa_salarial,
    grafico_ia_vs_salario,
    grafico_nivel_vs_salario,
)

st.set_page_config(
    page_title="Dashboard Mercado de Dados",
    layout="wide"
)

# =========================
# CARREGAMENTO DOS DADOS
# =========================

cargos_df = load_cargos()
linguagens_df = load_linguagens()
faixa_df = load_faixa_salarial()
ia_df = load_ia_salario()
nivel_df = load_nivel_salario()

# =========================
# TÍTULO
# =========================

st.title("📊 Dashboard de Indicadores do Mercado Tech")

st.markdown("""
Dashboard desenvolvido em Streamlit para visualização de KPIs
sobre salários, cargos, tecnologias e níveis profissionais.
""")

st.divider()

# =========================
# KPIs
# =========================

media_salarial = calcular_media_salarial(faixa_df)
tecnologia_principal = calcular_tecnologia_principal(linguagens_df)
amostra = calcular_amostra(cargos_df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="💰 Média Salarial",
        value=f"R$ {media_salarial:,.2f}"
    )

with col2:
    st.metric(
        label="💻 Tecnologia Principal",
        value=tecnologia_principal
    )

with col3:
    st.metric(
        label="👥 Amostra",
        value=f"{amostra:,}"
    )

st.divider()

# =========================
# GRÁFICOS
# =========================

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.plotly_chart(
        grafico_cargos(cargos_df),
        use_container_width=True
    )

with col_graf2:
    st.plotly_chart(
        grafico_linguagens(linguagens_df),
        use_container_width=True
    )

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    st.plotly_chart(
        grafico_faixa_salarial(faixa_df),
        use_container_width=True
    )

with col_graf4:
    st.plotly_chart(
        grafico_ia_vs_salario(ia_df),
        use_container_width=True
    )

st.plotly_chart(
    grafico_nivel_vs_salario(nivel_df),
    use_container_width=True
)