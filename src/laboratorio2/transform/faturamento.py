import pandas as pd
import logging

from laboratorio2.utils.utils import (
    tipagem_dados,
    padronizar_colunas,
    remover_duplicados,
    remover_prefixo_nf
)

logger = logging.getLogger(__name__)


def transformar_faturamento(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()

        logger.info(
            "Iniciando transformação faturamento, Registros: %d",
            len(df)
        )

        df = tipagem_dados(
            df,
            {
                "numero_nf": str,
                "data_faturamento": "datetime"
            }
        )

        df["numero_nf"] = df["numero_nf"].apply(
            remover_prefixo_nf
        )

        registro_antes = len(df)

        df = remover_duplicados(
            df,
            ["numero_nf", "id_pedido"]
        )

        logger.info(
            "Duplicados de faturamento removidos: %d",
            registro_antes - len(df)
        )

        df = padronizar_colunas(
            df,
            ["forma_pagamento", "status_faturamento"]
        )

        logger.info(
            "Transformações de faturamento concluídas. Registros: %d",
            len(df)
        )

        return df

    except Exception:
        logger.exception(
            "Erro ao transformar dados do faturamento"
        )
        raise


        