import pandas as pd
from pandas.testing import assert_frame_equal
from transform.categorias import transformar_categorias


def test_categoria ():

    dados_entrada = {
        "id_categoria": [10,22,10],
        "categoria": ["eletronicos", "informatica", "eletronicos"]
    }


    df = pd.DataFrame(dados_entrada)

    resultado = transformar_categorias(df)
    esperado = pd.DataFrame({
        "id_categoria": [10, 22],
        "categoria": ["Eletronicos", "Informatica"]
    })


    assert_frame_equal(resultado, esperado)