import pandas as pd
from utils.utils import (
    tipagem_dados,
    remover_duplicados,
    padronizar_colunas
)

import logging

logger = logging.getLogger(__name__)

def transformar_vendedores (df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()
        logging.info("Iniciando transformacoes dos vendedores: Registros: %d", len(df))

        registro_antes = len(df)


        df = remover_duplicados(
            df, ["id_vendedor", "nome_vendedor"])

        logger.info("Duplicados de vendedores removidos: %d", registro_antes - len(df))

        df = padronizar_colunas (
            df, ["nome_vendedor", "canal_venda"]
        )

        logger.info("Transformaçoes de vendedores concluidas. Registros: %d", len(df))

        return df 

    except Exception:
        logger.exception("Erro ao transformar dados dos vendedores")
        raise
    

        
