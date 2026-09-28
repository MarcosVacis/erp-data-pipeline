import logging

from laboratorio2.extract.extract import extradir_dados, carregar_dados
from laboratorio2.transform.transform import executar_transfomacoes


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        dados = extradir_dados()
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

    print(dados_transformados)


if __name__ == "__main__":
    main()
