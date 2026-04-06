from scripts.transformacao import gerar_dataset_final
from scripts.metricas import calcular_metricas

def main():
    print("Chamando transformação...")
    df = gerar_dataset_final()

    print("Chamando métricas...")
    calcular_metricas(df)

if __name__ == "__main__":
    main()