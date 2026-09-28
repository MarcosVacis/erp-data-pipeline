import pandas as pd
from laboratorio2.utils.utils import (
    tipagem_dados,
    remover_duplicados,
    padronizar_colunas
)

import logging

logger = logging.getLogger(__name__)

def transformar_produtos (df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()
        logging.info("Iniciando transformacoes dos produtos: Registros: %d", len(df))


        registro_antes = len(df)


        df = remover_duplicados(
            df, ["id_produto", "nome_produto"])

        logger.info("Duplicados de produtos removidos: %d", registro_antes - len(df))

        df = padronizar_colunas (
            df, ["nome_produto", "status"]
        )

        logger.info("Transformaçoes de produtos concluidas. Registros: %d", len(df))

        return df 

    except Exception:
        logger.exception("Erro ao transformar dados dos produtos")
        raise
    

        
