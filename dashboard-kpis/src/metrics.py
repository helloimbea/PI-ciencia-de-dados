import pandas as pd
import plotly.express as px


# =========================
# FUNÇÕES DE KPI
# =========================


def calcular_media_salarial(df):
    valores_medios = {
        "Menos de 1.000": 1000,
        "de 1.001 a 2.000": 1500,
        "de 2.001 a 3.000": 2500,
        "de 3.001 a 4.000": 3500,
        "de 4.001 a 6.000": 5000,
        "de 6.001 a 8.000": 7000,
        "de 8.001 a 12.000": 10000,
        "de 12.001 a 16.000": 14000,
        "de 16.001 a 20.000": 18000,
        "de 20.001 a 25.000": 22500,
        "de 25.001 a 30.000": 27500,
        "de 30.001 a 40.000": 35000,
        "Acima de 40.001": 45000,
    }

    total_salarios = 0
    total_pessoas = 0

    for _, row in df.iterrows():
        faixa = row["faixa_salarial_ordenada"]
        quantidade = row["quantidade"]

        if faixa in valores_medios:
            total_salarios += valores_medios[faixa] * quantidade
            total_pessoas += quantidade

    if total_pessoas == 0:
        return 0

    return total_salarios / total_pessoas



def calcular_tecnologia_principal(df):
    return df.loc[df["quantidade"].idxmax(), "linguagem"]



def calcular_amostra(df):
    return df["quantidade"].sum()

# =========================
# GRÁFICOS
# =========================


def grafico_cargos(df):
    fig = px.bar(
        df,
        x="cargo",
        y="quantidade",
        title="Distribuição de Cargos"
    )

    fig.update_layout(
        xaxis_title="Cargo",
        yaxis_title="Quantidade",
        xaxis_tickangle=-25
    )

    return fig



def grafico_linguagens(df):
    top_df = df.head(10)

    fig = px.pie(
        top_df,
        names="linguagem",
        values="quantidade",
        title="Top Tecnologias"
    )

    return fig

 
def grafico_faixa_salarial(df):
    fig = px.bar(
        df,
        x="faixa_salarial_ordenada",
        y="quantidade",
        title="Distribuição Salarial"
    )

    fig.update_layout(
        xaxis_tickangle=-35,
        xaxis_title="Faixa Salarial",
        yaxis_title="Quantidade"
    )

    return fig



def grafico_ia_vs_salario(df):
    melted_df = df.melt(
        id_vars="categoria_ia",
        var_name="faixa_salarial",
        value_name="quantidade"
    )

    fig = px.bar(
        melted_df,
        x="categoria_ia",
        y="quantidade",
        color="faixa_salarial",
        title="Uso de IA vs Faixa Salarial"
    )
    
    fig.update_layout(
        xaxis_title="Categoria IA",
        yaxis_title="Quantidade"
    )

    return fig



def grafico_nivel_vs_salario(df):
    melted_df = df.melt(
        id_vars="2.g_nivel",
        var_name="faixa_salarial",
        value_name="quantidade"
    )

    fig = px.density_heatmap(
        melted_df,
        x="faixa_salarial",
        y="2.g_nivel",
        z="quantidade",
        title="Nível Profissional vs Faixa Salarial"
    )

    fig.update_layout(
        xaxis_tickangle=-35
    )

    return fig