from scripts.transformacao import gerar_dataset_final
from scripts.metricas import calcular_metricas

def main():
    df = gerar_dataset_final()
    calcular_metricas(df)

    if __name__ == "__main__":
        main()
