import logging

from laboratorio2.extract.extract import extradir_dados
from laboratorio2.transform.transform import executar_transfomacoes
from laboratorio2.load.load import (
    executar_dim_categoria,
    executar_dim_cliente,
    executar_dim_produto,
    executar_dim_vendedor,
    executar_dim_data,
    executar_fato_vendas,
    executar_fato_faturamento,
)



def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # EXTRACT
    try:
        dados = extradir_dados()
        print("CHAVES DO DADOS:", dados.keys())

        logging.info("Dados extraídos com sucesso!")

    except Exception:
        logging.exception("Falha ao extrair os dados!")
        raise

    # TRANSFORM
    dados_transformados = executar_transfomacoes(
        categorias=dados["categoria"],
        clientes=dados["cliente"],
        faturamento=dados["faturamento"],
        itens_pedidos=dados["itens_pedido"],
        pedidos=dados["pedidos"],
        produtos=dados["produtos"],
        vendedores=dados["vendedores"]
    )

    # LOAD STAGING
    # try:
    #     carregar_staging(dados_transformados)

    # except Exception:
    #     logging.exception("Falha ao carregar a staging!")
    #     raise

    # LOAD DW
    try:
        executar_dim_categoria()
        executar_dim_cliente()
        executar_dim_produto()
        executar_dim_vendedor()
        executar_dim_data()

        executar_fato_vendas()
        executar_fato_faturamento()


    except Exception:
        logging.exception("Falha ao carregar dimensão categoria!")
        raise


if __name__ == "__main__":
    main()
