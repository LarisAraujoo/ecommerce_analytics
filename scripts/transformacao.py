import pandas as pd

def gerar_dataset_final():
    clientes = pd.read_csv("data/clientes.csv")
    itens = pd.read_csv("data/itens_pedido.csv")
    pedidos = pd.read_csv("data/pedidos.csv")
    produtos = pd.read_csv("data/produtos.csv")

    pedidos_itens = pd.merge(pedidos, itens, on="pedido_id")
    df_final = pd.merge(pedidos_itens, produtos, on="produto_id")

    df_final["fatturamento"] = df_final["quantidade"] * df_final["preco"]

    df_final.to_csv("data/dataset_final.csv", indx=False)
    print("Dataset final gerado.")

    return df_final