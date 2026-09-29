BEGIN;
INSERT INTO dw.dim_categoria (
    categoria_sk,
    id_categoria,
    categoria
)
SELECT
    nextval('dw.dim_categoria_categoria_sk_seq') as categoria_sk,
    c.id_categoria,
    c.categoria
FROM staging.categoria c
WHERE NOT EXISTS (
    SELECT 1
    FROM dw.dim_categoria cs
    WHERE cs.id_categoria = c.id_categoria
);
COMMIT