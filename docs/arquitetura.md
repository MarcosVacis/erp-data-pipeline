projeto_suporte_etl/
│
├── data/
│   ├── raw/
│   │   ├── clientes.csv
│   │   ├── agentes.csv
│   │   ├── tickets.csv
│   │   ├── interacoes.csv
│   │   └── sla_regras.csv
│   │
│   ├── processed/
│   │
│   └── curated/
│
├── src/
│   ├── extract/
│   │   └── extract.py
│   │
│   ├── transform/
│   │   └── transform.py
│   │
│   ├── validate/
│   │   └── validate.py
│   │
│   ├── load/
│   │   └── load.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── config.py
│   │
│   └── main.py
│
├── model/
│   └── schema.sql
│
├── sql/
│   └── queries_analise.sql
│
├── tests/
│   ├── test_transform.py
│   ├── test_validate.py
│   └── test_load.py
│
├── logs/
│
├── notebooks/
│
├── docs/
│   └── arquitetura.md
│
├── .gitignore
├── requirements.txt
└── README.md