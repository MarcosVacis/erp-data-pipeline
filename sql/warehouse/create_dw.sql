CREATE SCHEMA IF NOT EXISTS dw;

CREATE TABLE dw.dim_cliente (
    cliente_sk BIGSERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    cliente VARCHAR(150),
    email VARCHAR(150),
    estado CHAR(2),
    data_cadastro DATE,
    status VARCHAR(20)
);


CREATE TABLE dw.dim_produto (
    produto_sk BIGSERIAL PRIMARY KEY,
    id_produto INTEGER NOT NULL,
    id_categoria INTEGER,
    produto VARCHAR(100),
    custo_unitario NUMERIC(15,2),
    preco_tabela NUMERIC(15,2),
    status VARCHAR(20)
);


CREATE TABLE dw.dim_categoria (
    categoria_sk BIGSERIAL PRIMARY KEY,
    id_categoria INTEGER NOT NULL,
    categoria VARCHAR(50)
);


CREATE TABLE dw.dim_vendedor (
    vendedor_sk BIGSERIAL PRIMARY KEY,
    id_vendedor INTEGER NOT NULL,
    nome VARCHAR(150),
    estado CHAR(2),
    canal_venda VARCHAR(50)
);



CREATE TABLE dw.dim_data (
    data_sk INTEGER PRIMARY KEY,
    data DATE NOT NULL,
    ano INTEGER,
    mes INTEGER,
    nome_mes VARCHAR(20),
    trimestre INTEGER,
    dia INTEGER,
    dia_semana INTEGER,
    nome_dia_semana VARCHAR(20),
    fim_de_semana BOOLEAN
);


CREATE TABLE dw.fact_vendas (
    venda_sk BIGSERIAL PRIMARY KEY,

    id_pedido INTEGER NOT NULL,
    id_item INTEGER NOT NULL,

    data_sk INTEGER NOT NULL,
    cliente_sk BIGINT NOT NULL,
    produto_sk BIGINT NOT NULL,
    vendedor_sk BIGINT NOT NULL,

    quantidade INTEGER NOT NULL,

    preco_unitario NUMERIC(15,2),
    desconto_perc NUMERIC(5,4),

    valor_bruto NUMERIC(15,2),
    valor_desconto NUMERIC(15,2),
    valor_liquido NUMERIC(15,2),

    custo_unitario NUMERIC(15,2),

    FOREIGN KEY (data_sk)
        REFERENCES dw.dim_data(data_sk),

    FOREIGN KEY (cliente_sk)
        REFERENCES dw.dim_cliente(cliente_sk),

    FOREIGN KEY (produto_sk)
        REFERENCES dw.dim_produto(produto_sk),

    FOREIGN KEY (vendedor_sk)
        REFERENCES dw.dim_vendedor(vendedor_sk)
);



CREATE TABLE dw.fact_faturamento (
    faturamento_sk BIGSERIAL PRIMARY KEY,

    nf INTEGER NOT NULL,
    id_pedido INTEGER NOT NULL,

    data_sk INTEGER NOT NULL,
    cliente_sk BIGINT NOT NULL,

    forma_pagamento VARCHAR(30),
    status_faturamento VARCHAR(30),

    valor_faturamento NUMERIC(15,2),

    FOREIGN KEY (data_sk)
        REFERENCES dw.dim_data(data_sk),

    FOREIGN KEY (cliente_sk)
        REFERENCES dw.dim_cliente(cliente_sk)
);
