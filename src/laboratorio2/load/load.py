import logging

from sqlalchemy import create_engine


logger = logging.getLogger(__name__)


def criar_engine():
    return create_engine(
        "postgresql+psycopg://postgres:123456@localhost:5432/postgres"
    )


def carregar_staging(dados):
    engine = criar_engine()

    logger.info("Iniciando carga da staging")

    dados["clientes"].to_sql(
        "clientes",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.clientes carregada: %s registros",
        len(dados["clientes"])
    )

    dados["categorias"].to_sql(
        "categorias",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.categoria carregada: %s registros",
        len(dados["categorias"])
    )

    dados["faturamento"].to_sql(
        "faturamento",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.faturamento carregada: %s registros",
        len(dados["faturamento"])
    )

    dados["itens_pedidos"].to_sql(
        "itens_pedidos",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.itens_pedidos carregada: %s registros",
        len(dados["itens_pedidos"])
    )

    dados["pedidos"].to_sql(
        "pedido",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.pedido carregada: %s registros",
        len(dados["pedidos"])
    )

    dados["produtos"].to_sql(
        "produto",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.produto carregada: %s registros",
        len(dados["produtos"])
    )

    dados["vendedores"].to_sql(
        "vendedor",
        con=engine,
        schema="staging",
        if_exists="append",
        index=False
    )
    logger.info(
        "Tabela staging.vendedor carregada: %s registros",
        len(dados["vendedores"])
    )

    logger.info("Carga da staging concluída com sucesso")
