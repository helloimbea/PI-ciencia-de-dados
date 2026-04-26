import pandas as pd

def carregar_dados():
    df = pd.read_csv("data/raw/state_of_data_2024.csv")
    return df