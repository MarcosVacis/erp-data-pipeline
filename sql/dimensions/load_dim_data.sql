BEGIN;
INSERT INTO dw.dim_data (
    data_sk,
    data,
    ano,
    mes,
    nome_mes,
    trimestre,
    dia,
    dia_semana,
    nome_dia_semana,
    fim_de_semana
)
SELECT
    TO_CHAR(d, 'YYYYMMDD')::INTEGER AS data_sk,
    d::DATE AS data,
    EXTRACT(YEAR FROM d)::INTEGER AS ano,
    EXTRACT(MONTH FROM d)::INTEGER AS mes,
    TO_CHAR(d, 'TMMonth') AS nome_mes,
    EXTRACT(QUARTER FROM d)::INTEGER AS trimestre,
    EXTRACT(DAY FROM d)::INTEGER AS dia,
    EXTRACT(ISODOW FROM d)::INTEGER AS dia_semana,
    TO_CHAR(d, 'TMDay') AS nome_dia_semana,
    CASE
        WHEN EXTRACT(ISODOW FROM d) IN (6, 7) THEN TRUE
        ELSE FALSE
    END AS fim_de_semana
FROM generate_series(
    '2020-01-01'::DATE,
    '2030-12-31'::DATE,
    '1 day'::INTERVAL
) AS gs(d);

COMMIT;