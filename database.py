import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuration
DATABASE_URL_ENV_VAR = "DATABASE_URL"
DEFAULT_DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

# Load database URL from environment variable or use default
database_url = os.getenv(DATABASE_URL_ENV_VAR, DEFAULT_DATABASE_URL)

# Database Engine
async_engine = create_async_engine(database_url, echo=True)

# Session Configuration
Session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

# Declarative Base
Base = declarative_base()

# Optional: create all tables in the database
# Base.metadata.create_all(async_engine)