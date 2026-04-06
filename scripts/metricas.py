import matplotlib.pyplot as plt

def calcular_metricas(df):
    faturamento_total = df["faturamento"].sum()
    ticket_medio = df["faturamento"].mean()
    total_pedidos = df["pedido_id"].nunique()
    clientes_unicos = df["cliente_id"].nunique()

    print("Faturamento total:", faturamento_total)
    print("Ticket médio:", ticket_medio)
    print("Total de pedidos:", total_pedidos)
    print("Clientes únicos:", clientes_unicos)

    produtos_mais_vendidos = (
        df.groupby("nome")["quantidade"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nTop 10 produtos mais vendidos:")
    print(produtos_mais_vendidos.head(10))

    # GRÁFICO
    # -------------------------------
    produtos_mais_vendidos.head(10).plot(kind="bar")

    plt.title("Top 10 Produtos Mais Vendidos")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("data/top_produtos.png")
    plt.show()
