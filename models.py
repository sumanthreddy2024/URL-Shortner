from sqlalchemy import Column, Integer, String
from .database import Base

class WebAddress(Base):
    """Represents a URL entity in the database, 
    which can be used to redirect users to the original long URL using a shortened code."""
    __tablename__ = "urls"

    # Unique identifier for the URL
    url_id = Column(Integer, primary_key=True, index=True)

    # The original long URL that the user wants to shorten
    original_url = Column(String, index=True)

    # The shortened code that can be used to redirect users to the original URL
    shortened_code = Column(String, unique=True, index=True)