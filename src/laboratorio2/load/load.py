import logging
from laboratorio2.database.executor import executar_sql
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy import text

from laboratorio2.database.engine import criar_engine


logger = logging.getLogger(__name__)



# def carregar_staging(dados):
    # engine = criar_engine()

    # logger.info("Iniciando carga da staging")

    # dados["clientes"].to_sql(
    #     "clientes",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.clientes carregada: %s registros",
    #     len(dados["clientes"])
    # )

    # dados["categorias"].to_sql(
    #     "categoria;",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.categoria carregada: %s registros",
    #     len(dados["categorias"])
    # )

    # dados["faturamento"].to_sql(
    #     "faturamento",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.faturamento carregada: %s registros",
    #     len(dados["faturamento"])
    # )

    # dados["itens_pedidos"].to_sql(
    #     "itens_pedidos",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.itens_pedidos carregada: %s registros",
    #     len(dados["itens_pedidos"])
    # )

    # dados["pedidos"].to_sql(
    #     "pedido",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.pedido carregada: %s registros",
    #     len(dados["pedidos"])
    # )

    # dados["produtos"].to_sql(
    #     "produto",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.produto carregada: %s registros",
    #     len(dados["produtos"])
    # )

    # dados["vendedores"].to_sql(
    #     "vendedor",
    #     con=engine,
    #     schema="staging",
    #     if_exists="append",
    #     index=False
    # )
    # logger.info(
    #     "Tabela staging.vendedor carregada: %s registros",
    #     len(dados["vendedores"])
    # )

    # logger.info("Carga da staging concluída com sucesso")


def executar_dim_cliente():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "dimensions"
        / "load_dim_cliente.sql"
    )

    executar_sql(caminho_sql)


def executar_dim_categoria():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "dimensions"
        / "load_dim_categoria.sql"
    )

    executar_sql(caminho_sql)


def executar_dim_produto():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "dimensions"
        / "load_dim_produto.sql"
    )

    executar_sql(caminho_sql)


def executar_dim_vendedor():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "dimensions"
        / "load_dim_vendedor.sql"
    )

    executar_sql(caminho_sql)


def executar_dim_data():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "dimensions"
        / "load_dim_data.sql"
    )

    executar_sql(caminho_sql)


def executar_fato_vendas():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "facts"
        / "load_fact_vendas.sql"
    )

    executar_sql(caminho_sql)


def executar_fato_faturamento():
    caminho_sql = (
        Path(__file__).resolve().parents[3]
        / "sql"
        / "facts"
        / "load_fact_faturamento.sql"
    )

    executar_sql(caminho_sql)