import logging
from pathlib import Path
from sqlalchemy import text
from laboratorio2.database.engine import criar_engine


logger = logging.getLogger(__name__)


def executar_sql (caminho_sql: Path):
    engine = criar_engine ()

    logger.info ("Executando SQL: %s", caminho_sql)
    sql = caminho_sql.read_text(encoding= "utf-8")

    try:
        with engine.begin() as conn:
            conn.execute(text(sql))

        logger.info("SQL executado com sucesso: %s",caminho_sql)
    except Exception:
        logger.exception ("Erro ao executar SQL: %s", caminho_sql)
        raise