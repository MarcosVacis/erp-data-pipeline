import pandas as pd
from pandas.testing import assert_frame_equal
from transform.clientes import transformar_cliente


def test_clientes():
    dados_entrada = {
        "nome_cliente": ["mArcos Daniel", "marcos Costa"],
        "id_cliente": [1, 1],
        "data_cadastro": ['2026-09-22', '2026-09-21'],
        "status": ["Ativo", "Inativo"]
    }

    df = pd.DataFrame(dados_entrada)


    resultado = transformar_cliente(df)
    esperado = pd.DataFrame({
        "nome_cliente": ["Marcos Daniel", "Marcos Costa"],
        "id_cliente": [1, 1],
        "data_cadastro": pd.to_datetime(['2026-09-22', '2026-09-21']),
        "status": ["Ativo", "Inativo"]
    })
    
    
    assert_frame_equal(resultado, esperado)