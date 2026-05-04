def calcular_kpis(df):
    kpis = {}

    if "salario" in df.columns:
        kpis["media_salario"] = df["salario"].mean()
        kpis["mediana_salario"] = df["salario"].median()

    if "idade" in df.columns:
        kpis["media_idade"] = df["idade"].mean()

    return kpis