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

faturamento_total = df_final["faturamento"].sum()
print("Faturamento total da empresa:", faturamento_total)
