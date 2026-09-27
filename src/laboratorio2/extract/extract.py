import logging
from pathlib import Path
import pandas as pd

from laboratorio2.utils.config import DIR_RAW

logger = logging.getLogger(__name__)


def carregar_dados(caminho: Path, nome_dataset: str) -> pd.DataFrame:
    """Carrega um arquivo CSV a partir de um Path."""
    logger.info("Verificando arquivo: %s", caminho)

    if not caminho.exists():
        logger.error("Arquivo não encontrado: %s", caminho)
        raise FileNotFoundError(f"O arquivo {caminho} não existe.")

    try:
        df = pd.read_csv(caminho)
        logger.info(
            "Dataset '%s' carregado com sucesso. Linhas: %d",
            nome_dataset,
            len(df)
        )
        return df

    except Exception:
        logger.exception(
            "Erro inesperado ao carregar o dataset '%s': %s",
            nome_dataset,
            caminho
        )
        raise


def extradir_dados() -> dict:
    logger.info("Iniciando a extração dos dados....")

    dados_bruto = {
        "categoria": carregar_dados(
            DIR_RAW / "categorias.csv",
            "categoria"
        ),
        "cliente": carregar_dados(
            DIR_RAW / "clientes.csv",
            "cliente"
        ),
        "faturamento": carregar_dados(
            DIR_RAW / "faturamentos.csv",
            "faturamento"
        ),
        "itens_pedido": carregar_dados(
            DIR_RAW / "itens_pedido.csv",
            "itens_pedido"
        ),
        "pedidos": carregar_dados(
            DIR_RAW / "pedidos.csv",
            "pedidos"
        ),
        "produtos": carregar_dados(
            DIR_RAW / "produtos.csv",
            "produtos"
        ),
        "vendedores": carregar_dados(
            DIR_RAW / "vendedores.csv",
            "vendedores"
        )
    }

    return dados_bruto
