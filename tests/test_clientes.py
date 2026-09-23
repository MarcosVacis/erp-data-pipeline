import pandas as pd
from pandas.testing import assert_frame_equal
from transform.clientes import transformar_cliente


def test_clientes():
    # Dados de entrada (o pytest aceita dicionário se sua função converter para DataFrame,
    # ou você já pode passar um pd.DataFrame se preferir)
    dados_entrada = {
        "nome_cliente": ["mArcos Daniel", "marcos Costa"],
        "id_cliente": [1, 1],
        "data_cadastro": ['2026-09-22', '2026-09-21'],
        "status": ["Ativo", "Inativo"]
    }

    df = pd.DataFrame(dados_entrada)

    # 1. Executa a função passando os dados
    resultado = transformar_cliente(df)
    esperado = pd.DataFrame({
        "nome_cliente": ["Marcos Daniel", "Marcos Costa"],
        "id_cliente": [1, 1],
        "data_cadastro": pd.to_datetime(['2026-09-22', '2026-09-21']),
        "status": ["Ativo", "Inativo"]
    })
    
    # Força a mesma precisão de nanosegundos
    esperado["data_cadastro"] = esperado["data_cadastro"].astype("datetime64[ns]")
    # 3. Faz a asserção garantindo que os DataFrames são iguais
    assert_frame_equal(resultado, esperado)