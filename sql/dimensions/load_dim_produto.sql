BEGIN;
INSERT  INTO dw.dim_produto(
    produto_sk,
    id_produto,
    id_categoria,
    produto,
    custo_unitario,
    preco_tabela,
    status
)
SELECT
    nextval('dw.dim_produto_produto_sk_seq') as produto_sk,
    prod.id_produto,
    prod.id_categoria,
    prod.nome_produto as produto,
    prod.custo_unitario,
    prod.preco_tabela,
    prod.status
FROM staging.produto prod
WHERE NOT EXISTS(
    SELECT  1 FROM dw.dim_produto pt where pt.id_produto = prod.id_produto
);
COMMIT ;
