BEGIN;

INSERT INTO dw.fact_faturamento (
    faturamento_sk,
    nf,
    id_pedido,
    data_sk,
    cliente_sk,
    forma_pagamento,
    status_faturamento,
    valor_faturamento
)
SELECT
    nextval('dw.fact_faturamento_faturamento_sk_seq') AS faturamento_sk,
    fat.numero_nf AS nf,
    fat.id_pedido,
    dt.data_sk,
    cli.cliente_sk,
    fat.forma_pagamento,
    fat.status_faturamento,
    fat.valor_faturado
FROM staging.faturamento fat

JOIN dw.dim_data dt
    ON dt.data = fat.data_faturamento

JOIN staging.pedido ip
    ON ip.id_pedido = fat.id_pedido

JOIN dw.dim_cliente cli
    ON cli.id_cliente = ip.id_cliente

WHERE NOT EXISTS (
    SELECT 1
    FROM dw.fact_faturamento ft
    WHERE ft.id_pedido = fat.id_pedido
      AND ft.cliente_sk = cli.cliente_sk
      AND ft.nf = fat.numero_nf
);

COMMIT;
