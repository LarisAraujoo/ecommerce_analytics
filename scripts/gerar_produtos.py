import pandas as pd
import random

produtos = []

categorias = ["Roupas", "Calçados", "Acessórios"]

for i in range(50):
    produto = {
        "produto_id": i,
        "nome": f"Produto_{i}",
        "categoria": random.choice(categorias),
        "preco": random.randint(50, 500)
    }
    produtos.append(produto)

    df = pd.DataFrame(produtos)
    df.to_csv("data/produtos.csv", index=False)