import pandas as pd
import logging

from laboratorio2.utils.utils import (
    tipagem_dados,
    padronizar_colunas,
    remover_duplicados
)

logger = logging.getLogger(__name__)


def transformar_faturamento (df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()
        logger.info("Iniciando transfomacao faturamento, Registros: %d", len(df))

        df = tipagem_dados(
            df, {
                "numero_nf": int,
                "data_faturamento": "datetime"

            })

        registro_antes = len(df)

        df = remover_duplicados (
            df, ["numero-nf", "id_pedido"]
        )

        logger.info("Duplicados de faturamento removidos: %d", registro_antes - len(df))

        df = padronizar_colunas(
            df, ["forma_pagament", "status-faturamento"])

        logger.info("Transformacoes de faturamento concluidas. Registros: %d", len(df))

        return df
    except Exception:
        logger.exception("Erro ao transformar dados do faturamento")
        raise


        