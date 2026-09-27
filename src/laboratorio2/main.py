import logging

from laboratorio2.extract.extract import extradir_dados, carregar_dados
from laboratorio2.transform.transform import executar_transfomacoes


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    dados = extradir_dados()

    clientes = dados['cliente']

    print(clientes)


if __name__ == "__main__":
    main()
