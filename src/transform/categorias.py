import pandas as pd
from utils.utils import(

tipagem_dados,
remover_duplicados,
padronizar_colunas
)

import logging

logger = logging.getLogger(__name__)





def transformar_categorias (df:pd.DataFrame ) -> pd.DataFrame:
    try:
        df = df.copy()
        logger.info("Iniciando transfomacoes das categorias: Registro: %d", len(df))


        df = tipagem_dados(df, {
            "id_categoria": int,
            "categoria": str
        })

        registros_antes = len(df)

        df = remover_duplicados (
            df,["id_categoria", "categoria"])

        logger.info("Duplicados de clientes removidos: %d", registros_antes - len(df))

        df = padronizar_colunas(df, ["categoria"])

        logger.info("Transformacoes de categorias concluidas. Registos: %d", len(df))

        return df
    except Exception:
        logger.exception("Erro ao transformar dados de categoria")
        raise