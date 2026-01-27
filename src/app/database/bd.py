from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://root:ntt_projeto@localhost:3307/ntt_projeto"

engine = create_engine(
    DATABASE_URL,
    echo=True  # mostra SQL gerado (útil em dev)
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()