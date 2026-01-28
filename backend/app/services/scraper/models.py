from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class PropertyListing(BaseModel):
    title: str
    price: str
    location: str
    bedrooms: Optional[str] = None
    bathrooms: Optional[str] = None
    area_sqft: Optional[str] = None
    url: str
    source: str # e.g. "Bayut", "Property Finder"
    image_url: Optional[str] = None

class ScrapeResult(BaseModel):
    query: str
    results: List[PropertyListing]
    count: int
