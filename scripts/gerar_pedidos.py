import pandas as pd
import random
from datetime import datetime, timedelta

pedidos = []

status_opcoes = ["Entregue", "Cancelado", "Em transporte"]

for i in range(200):
    data_pedido = datetime.now() - timedelta(days=random.randint(0, 365))

    pedido = {
        "pedido_id": i,
        "cliente_id": random.randint(0, 99),
        "data_pedido": data_pedido,
        "status": random.choice(status_opcoes)
    }

    pedidos.append(pedido)

df = pd.DataFrame(pedidos)
df.to_csv("data/pedidos.csv", index=False)