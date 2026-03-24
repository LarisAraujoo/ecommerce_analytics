import pandas as pd
import random

itens = []

for i in range(500):
    item = {
        "item_id": i,
        "pedido_id": random.randint(0, 199),
        "produto_id": random.randint(0, 49),
        "quantidade": random.randint(1, 5)
    }

    itens.append(item)

df = pd.DataFrame(itens)
df.to_csv("data/itens_pedido.csv", index=False)