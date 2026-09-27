import logging
from pathlib import Path
import pandas as pd

from utils.config import DIR_RAW

logger = logging.getLogger(__name__)


def carregar_dados(caminho: Path) -> pd.DataFrame:
    """Carrega um arquivo CSV a partir de um Path."""
    logger.info("Verificando arquivo: %s", caminho)

    #  Valida se o arquivo realmente existe antes de ler
    if not caminho.exists():
        logger.error("Arquivo não encontrado: %s", caminho)
        raise FileNotFoundError(f"O arquivo {caminho} não existe.")

    try:
        # Lê o arquivo passando o caminho corretamente
        df = pd.read_csv(caminho)
        logger.info("Arquivo carregado com sucesso. Linhas: %d", len(df))
        return df

    except Exception:
        logger.exception("Erro inesperado ao carregar o arquivo: %s", caminho)
        raise

def extradir_dados () -> dict:
    logger.info("Iniciando a extração dos dados....")


    dados_bruto = {
        "categoria": carregar_dados(DIR_RAW / "categorias.csv"),
        "cliente": carregar_dados(DIR_RAW / "clientes.csv"),
        "faturamento": carregar_dados(DIR_RAW / "faturamentos.csv"),
        "itens_pedido": carregar_dados(DIR_RAW / "itens_pedido.csv"),
        "pedidos": carregar_dados(DIR_RAW / "pedidos.csv"),
        "produtos": carregar_dados(DIR_RAW / "produtos.csv"),
        "vendedores": carregar_dados(DIR_RAW / "vendedores.csv")
    
    }

    return dados_bruto