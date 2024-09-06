from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
import shortuuid

# Database Configuration
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

# Create the database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# Create a base class for declarative models
Base = declarative_base()

# Define the FastAPI app
app = FastAPI()

# Define the URL model
class URL(Base):
    __tablename__ = "urls"
    url_id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, index=True)
    short_code = Column(String, unique=True, index=True)
    def __str__(self):
        return f"URL(id={self.id}, long_url={self.long_url}, short_code={self.short_code})"

# Define the URLCreate model
class URLCreate(BaseModel):
    long_url: str

    def __str__(self):
        return f"URLCreate(long_url={self.long_url})"

# Define a dependency to get a database session
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

# Define the endpoint to create a short URL
@app.post("/shorten")
async def create_short_url(url: URLCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new short URL for the given long URL.
    """
    short_code = shortuuid.ShortUUID().random(length=6)
    db_url = URL(long_url=url.long_url, short_code=short_code)
    db.add(db_url)
    await db.commit()
    await db.refresh(db_url)
    return {"short_url": f"http://localhost:8000/{short_code}"}

# Define the endpoint to redirect to the original URL
@app.get("/{short_code}")
async def redirect_url(short_code: str, db: AsyncSession = Depends(get_db)):
    """
    Redirect to the original URL for the given short code.
    """
    query = select(URL).where(URL.short_code == short_code)
    result = await db.execute(query)
    db_url = result.scalar()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": db_url.long_url}