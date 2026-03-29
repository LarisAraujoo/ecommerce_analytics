import pandas as pd

clientes = pd.read_csv("data/clientes.csv")
itens = pd.read_csv("data/itens_pedido.csv")
pedidos = pd.read_csv("data/pedidos.csv")
produtos = pd.read_csv("data/produtos.csv")


print(clientes.head())

print(clientes.shape)
print(itens.shape)
print(pedidos.shape)
print(produtos.shape)

print(clientes.info())

pedidos_itens = pd.merge(pedidos, itens, on="pedido_id")
print(pedidos_itens.head())

df_final = pd.merge(pedidos_itens, produtos, on="produto_id")

df_final["faturamento"] = df_final["quantidade"] * df_final["preco"]

# Faturamento total
faturamento_total = df_final["faturamento"].sum()
print("Faturamento total da empresa:", faturamento_total)

# Ticket médio
ticket_medio = df_final["faturamento"].mean()
print("Ticket médio:", ticket_medio)

# Total de pedidos
total_pedidos = df_final["pedido_id"].nunique()
print("Total de pedido:", total_pedidos)

# Clientes únicos
clientes_unicos = df_final["cliente_id"].nunique()
print("Clientes únicos:", clientes_unicos)


# Produtos mais vendidos
produtos_mais_vendidos = (
    df_final
    .groupby("nome")["quantidade"]
    .sum()
    .sort_values(ascending=False)
)

print("Top 10 produtos mais vendidos:")
print(produtos_mais_vendidos.head(10))

df_final.to_csv("data/dataset_final.csv", index=False)
print("Dataset final salvo em data/dataset_final.csv")