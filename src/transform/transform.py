from extract.extract import carregar_dados
import pandas as pd
import logging

logger = logging.getLogger(__name__)


# def transformar_cliente (df: pd.DataFrame) -> pd.DataFrame:
#     return 0;


def tipagem_dados(df: pd.DataFrame, tipos: dict) -> pd.DataFrame:
    for coluna, tipo in tipos.items():
        try:
            df[coluna] = df[coluna].astype(tipo)
        except (ValueError, TypeError) as e:
            raise ValueError(
                f"Erro ao converter a coluna '{coluna}' para '{tipo}'"
            ) from e

    return df



def remover_duplicados (df: pd.DataFrame, colunas: list[str]) -> pd.DataFrame:
    return df.drop_duplicates(subset=colunas)


def padronizar_colunas (df: pd.DataFrame, colunas: list[str]) -> pd.DataFrame:
    df = df.copy()

    for coluna in colunas:
        df [coluna] = df[coluna].str.strip().str.title()
    return df

