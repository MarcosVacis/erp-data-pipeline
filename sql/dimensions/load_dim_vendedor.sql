BEGIN;

INSERT INTO dw.dim_vendedor (
    vendedor_sk,
    id_vendedor,
    nome,
    estado,
    canal_venda
)
SELECT
    nextval('dw.dim_vendedor_vendedor_sk_seq') as vendedor_sk,
    id_vendedor,
    nome_vendedor,
    estado,
    canal_venda
from staging.vendedor v
WHERE NOT EXISTS(
SELECT 1 FROM dw.dim_vendedor v2 where v2.id_vendedor = v.id_vendedor
);
COMMIT ;