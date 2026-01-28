from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from app.services.scraper.service import scraper_service

class SearchPropertiesInput(BaseModel):
    query: str = Field(description="Natural language query for property search (e.g., '2 bedroom apartment in Dubai Marina under 2M').")

class SearchPropertiesTool(BaseTool):
    name: str = "search_properties"
    description: str = "Search for real estate properties in Dubai using a natural language query."
    args_schema: Type[BaseModel] = SearchPropertiesInput

    def _run(self, query: str):
        raise NotImplementedError("Use _arun for async tool.")

    async def _arun(self, query: str):
        result = await scraper_service.search_properties(query)
        # Format for LLM consumption
        if not result.results:
            return "No properties found matching your criteria."
        
        response = f"Found {result.count} properties for '{result.query}':\n"
        for item in result.results:
            response += f"- {item.title} ({item.price}) in {item.location}. [Link]({item.url})\n"
        return response

class ROICalculatorInput(BaseModel):
    price: float = Field(description="Property price in AED")
    annual_rent: float = Field(description="Expected annual rent in AED")
    service_charges: float = Field(description="Annual service charges in AED", default=0.0)

class ROICalculatorTool(BaseTool):
    name: str = "calculate_roi"
    description: str = "Calculate Gross and Net ROI for a property."
    args_schema: Type[BaseModel] = ROICalculatorInput

    def _run(self, price: float, annual_rent: float, service_charges: float = 0.0):
        gross_roi = (annual_rent / price) * 100
        net_income = annual_rent - service_charges
        net_roi = (net_income / price) * 100
        
        return {
            "gross_roi_percent": round(gross_roi, 2),
            "net_roi_percent": round(net_roi, 2),
            "net_income": net_income
        }
    
    async def _arun(self, price: float, annual_rent: float, service_charges: float = 0.0):
        return self._run(price, annual_rent, service_charges)
