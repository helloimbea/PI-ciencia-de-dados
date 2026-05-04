import pandas as pd

def limpar_dados(df):
    # padronizar colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # remover duplicados
    df = df.drop_duplicates()

    # remover colunas vazias
    df = df.dropna(axis=1, how="all")

    # tratar valores nulos corretamente
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna("não informado")

    return df

def criar_features(df):
    if "salario" in df.columns:
        df["salario_anual"] = df["salario"] * 12

    if "anos_experiencia" in df.columns:
        df["senioridade"] = df["anos_experiencia"].apply(
            lambda x: "junior" if x < 2 else "pleno" if x < 5 else "senior"
        )

    return df