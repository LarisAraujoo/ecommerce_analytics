import pandas as pd
from faker import Faker

fake = Faker("pt-BR")

clientes = []

for i in range(100):
 cliente = {
    "cliente_id": i,
    "nome": fake.name(),
    "cidade": fake.city(),
    "estado": fake.state()
}
 clientes.append(cliente) 

df = pd.DataFrame(clientes)
df.to_csv("data/clientes.csv", index=False)