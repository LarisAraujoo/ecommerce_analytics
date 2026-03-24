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