from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from app.models.base import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    currency = Column(String, default="AED")
    
    # Location
    location = Column(String, index=True) # Full address
    area_name = Column(String, index=True) # e.g. "Dubai Marina"
    
    # Features
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    size_sqft = Column(Float)
    
    # Investment Metrics (Calculated)
    estimated_rent_yearly = Column(Float)
    roi_percentage = Column(Float)
    
    # External Data
    source_url = Column(String)
    images = Column(JSON) # List of image URLs
    
    # AI Embeddings (for search)
    embedding = Column(Vector(1536)) # OpenAI embedding dimension
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
