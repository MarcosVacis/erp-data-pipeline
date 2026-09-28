import logging

from laboratorio2.extract.extract import extradir_dados
from laboratorio2.transform.transform import executar_transfomacoes
from laboratorio2.load.load import carregar_staging


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        dados = extradir_dados()
        print("CHAVES DO DADOS:", dados.keys())

        logging.info("Dados extraídos com sucesso!")


    except Exception:
        logging.exception("Falha ao extrair os dados!")
        raise

    dados_transformados = executar_transfomacoes(
    categorias=dados["categoria"],
    clientes=dados["cliente"],
    faturamento=dados["faturamento"],
    itens_pedidos=dados["itens_pedido"],
    pedidos=dados["pedidos"],
    produtos=dados["produtos"],
    vendedores=dados["vendedores"]
    )


    try:
        carregar_staging(dados_transformados)

    except Exception:
        logging.exception("Falha ao carregar a staging!")
        raise


if __name__ == "__main__":
    main()
