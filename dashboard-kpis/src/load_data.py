import pandas as pd

BASE_PATH = "data/processed/"


def load_cargos():
    return pd.read_csv(BASE_PATH + "contagem_cargos.csv")


def load_linguagens():
    return pd.read_csv(BASE_PATH + "contagem_linguagens.csv")


def load_faixa_salarial():
    return pd.read_csv(BASE_PATH + "faixa_salarial.csv")


def load_ia_salario():
    return pd.read_csv(BASE_PATH + "ia_vs_salario.csv")


def load_nivel_salario():
    return pd.read_csv(BASE_PATH + "nivel_vs_salario_matriz.csv")