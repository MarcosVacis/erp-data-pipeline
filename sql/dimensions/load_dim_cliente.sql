BEGIN;
insert into dw.dim_cliente (
    cliente_sk,
    id_cliente,
    cliente,
    email,
    estado,
    data_cadastro,
    status
)
select distinct
    nextval('dw.dim_cliente_cliente_sk_seq') as cliente_sk,
    id_cliente,
    nome_cliente as cliente,
    email as email,
    estado as estado,
    data_cadastro as data_cadastro,
    status as status
from staging.clientes s
where not exists(
    select 1 from dw.dim_cliente d where d.id_cliente = s.id_cliente
);
commit;