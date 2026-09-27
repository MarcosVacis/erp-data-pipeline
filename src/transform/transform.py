from transform.categorias import transformar_categorias
from transform.clientes import transformar_cliente
from transform.faturamento import transformar_faturamento
from transform.itens_pedido import transformar_itens_pedidos
from transform.pedidos import transformar_pedidos
from transform.produtos import transformar_produtos
from transform.vendedores import transformar_vendedores

import logging

logger = logging.getLogger(__name__)


def executar_transfomacoes(
    categorias,
    clientes,
    faturamento,
    itens_pedidos,
    pedidos,
    produtos,
    vendedores
):
    categorias_tratadas = transformar_categorias(categorias)
    clientes_tratados = transformar_cliente(clientes)
    vendedores_tratados = transformar_vendedores(vendedores)
    produtos_tratados = transformar_produtos(produtos)
    pedidos_tratados = transformar_pedidos(pedidos)
    itens_pedidos_tratados = transformar_itens_pedidos(itens_pedidos)
    faturamento_tratados = transformar_faturamento(faturamento)

    return {
        "categorias": categorias_tratadas,
        "clientes": clientes_tratados,
        "faturamento": faturamento_tratados,
        "itens_pedido": itens_pedidos_tratados,
        "pedidos": pedidos_tratados,
        "produtos": produtos_tratados,
        "vendedores": vendedores_tratados
    }
