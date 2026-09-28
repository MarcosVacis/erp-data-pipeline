INSERT INTO dw.fact_vendas (
    id_pedido,
    id_item,
    data_sk,
    cliente_sk,
    produto_sk,
    vendedor_sk,
    quantidade,
    preco_unitario,
    desconto_perc,
    valor_bruto,
    valor_desconto,
    valor_liquido,
    custo_unitario
)
SELECT
    p.ID_PEDIDO,
    i.ID_ITEM,
    TO_CHAR(p.DATA_PEDIDO, 'YYYYMMDD')::INTEGER,
    c.cliente_sk,
    pr.produto_sk,
    v.vendedor_sk,
    i.QUANTIDADE,
    i.PRECO_UNITARIO,
    i.DESCONTO_PERC,
    i.VALOR_BRUTO,
    i.VALOR_DESCONTO,
    i.VALOR_LIQUIDO,
    i.CUSTO_UNITARIO
FROM staging.itens_pedidos i
JOIN staging.pedido p
    ON p.ID_PEDIDO = i.ID_PEDIDO
JOIN dw.dim_cliente c
    ON c.id_cliente = p.ID_CLIENTE
JOIN dw.dim_produto pr
    ON pr.id_produto = i.ID_PRODUTO
JOIN dw.dim_vendedor v
    ON v.id_vendedor = p.ID_VENDEDOR;
