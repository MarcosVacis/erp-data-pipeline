# ERP Data Pipeline

Pipeline de dados desenvolvido para simular o processamento
de dados de um sistema ERP.

O projeto realiza a extracao, transformacao, validacao,
modelagem e carga dos dados em um banco PostgreSQL.

## Arquitetura

CSV
 ERP / Dados de origem
        │
        ▼
     DATA RAW
        │
        ▼
      EXTRACT
        │
        ▼
     STAGING
        │
        ▼
    TRANSFORM
        │
        ▼
     VALIDATE
        │
        ▼
    PROCESSED
        │
        ▼
      MODEL
        │
        ▼
     CURATED
        │
        ▼
    POSTGRESQL
        │
        ▼
      BI / SQL

## Dados

O projeto utiliza dados simulados de um sistema ERP:

- clientes
- vendedores
- categorias
- produtos
- pedidos
- itens de pedido
- faturamentos

## Tecnologias

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Docker
- Apache Airflow
- Git

## Estrutura do projeto

```text
src/
data/
tests/
sql/