import logging
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


def criar_engine():
    return create_engine(
        "postgresql+psycopg://postgres:123456@localhost:5432/postgres"
    )