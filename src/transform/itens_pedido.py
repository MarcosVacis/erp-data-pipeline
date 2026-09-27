import pandas as pd
from utils.utils import (
    remover_duplicados,
)

import logging

logger = logging.getLogger(__name__)

def transformar_itens_pedidos (df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()
        logging.info("Iniciando transformacoes dos itens_pedidos: Registros: %d", len(df))

        registro_antes = len(df)


        df = remover_duplicados(
            df, ["id_item", "id_pedido", "id_produto"])

        logger.info("Duplicados de itens_pediddos removidos: %d", registro_antes - len(df))

        logger.info("Transformaçoes de itens_pedidos concluidas. Registros: %d", len(df))

        return df 

    except Exception:
        logger.exception("Erro ao transformar dados dos itens_pedidos")
        raise


        
