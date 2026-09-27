import pandas as pd
from pandas.testing import assert_frame_equal
from transform.pedidos import transfomar_pedidos



def test_pedidos ():
    dados_entrada = {
        "status_pedido": ["faturado", "faturado"],
        "id_pedido": [1, 1],
        "id_cliente": [17,17],
        "id_vendedor": [7, 7],
        "data_pedido": pd.to_datetime('2025-12-12')
    }


    df = pd.DataFrame(dados_entrada)

    resultado = transfomar_pedidos(df)

    esperado = pd.DataFrame (
        {
        "status_pedido": ["Faturado"],
        "id_pedido": [1],
        "id_cliente": [17],
        "id_vendedor": [7],
        "data_pedido": pd.to_datetime('2025-12-12')
    })

    assert_frame_equal(resultado, esperado)