import pandas as pd
import logging
from datetime import datetime

from utils.utils import(
tipagem_dados,
padronizar_colunas,
remover_duplicados
)

logger = logging.getLogger(__name__)


def transformar_cliente (df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()
        logger.info("Iniciando a trasnformacao de clientes. Registros: %d", len(df))

        df = tipagem_dados(
            df, {"data_cadastro":"datetime"}
        )

        registro_antes = len(df)

        df = remover_duplicados(
                df, ["id_cliente", "status"]
        ) 

        logger.info("Duplicados de clientes removidos: %d", registro_antes - len(df))

        df = padronizar_colunas(df, ["nome_cliente", "status"])

        logger.info("Transfomacoes de clientes concluidas. Registros: %d", len(df))

        return df
    except Exception:
        logger.exception("Erro ao transformar dados de clientes")
        raise