import pandas as pd

produtos = []

categorias = ["Roupas", "Calçados", "Acessórios"]

for i in range(50):
    produto = {
        "produto_id": i,
        "nome": f"Produto_{i}"
    }