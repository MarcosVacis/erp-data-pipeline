import pandas as pd
from utils.utils import (
    tipagem_dados,
    remover_duplicados,
    padronizar_colunas
)

import logging

logger = logging.getLogger(__name__)

def transformar_pedidos (df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()
        logging.info("Iniciando transformacoes dos pedidos: Registros: %d", len(df))

        df = tipagem_dados(
            df, {"data_pedido": "datetime"})

        registro_antes = len(df)


        df = remover_duplicados(
            df, ["id_pedido", "id_vendedor", "data_pedido"])

        logger.info("Duplicados de pediddos removidos: %d", registro_antes - len(df))

        df = padronizar_colunas (
            df, ["status_pedido"]
        )

        logger.info("Transformaçoes de pedidos concluidas. Registros: %d", len(df))

        return df 

    except Exception:
        logger.exception("Erro ao transformar dados dos pedidos")
        raise
    

        
