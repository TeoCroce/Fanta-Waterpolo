import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Database URL (devi assicurarti che user:password e il DB name siano corretti per il tuo Postgres)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/fanta_waterpolo_db_LOCAL") 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 2. Creazione dell'Engine di connessione
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

# 3. Creazione della Sessione
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base dichiarativa (usata dai modelli per ereditare la struttura della tabella)
Base = declarative_base()

# 5. Dependency per la Sessione di Database (da usare negli endpoint di FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()