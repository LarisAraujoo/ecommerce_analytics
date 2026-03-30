def calcular_metricas(df):
    faturamento_total = df["faturamento"].sum()
    ticket_medio = df["faturamento"].mean()
    total_pedidos = df["pedidos_id"].nunique()
    clientes_unicos = df["clientes_id"].nunique()

    print("Faturamento total:", faturamento_total)
    print("Ticket médio:", ticket_medio)
    print("Total de pedidos:", total_pedidos)
    print("Clientes únicos:", clientes_unicos)

    produtos_mais_vendidos = (
        df.goupby("nome")["quantidade"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop 10 produtos mais vendidos:")
    print(produtos_mais_vendidos.head(10))
