import os
import requests
from dotenv import load_dotenv
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# Load environment variables from .env file 
load_dotenv()

class EnrichCompanyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    domain: str = Field(..., description="Domain of the company(eg: example.com)")

class EnrichCompanyTool(BaseTool):
    name: str = "Enrich Company Information tool using The Companies API"
    description: str = (
        "Enhance the companies with additional information"
    )
    args_schema: Type[BaseModel] = EnrichCompanyToolInput

    def _run(self, domain: str) -> str:
        """
            Executes the "Companies API" tool to discover additional company details.

            @Args:
                domain(str):- Domain of the company(eg: example.com)
            @Returns:
                A string containing the enriched company information
        """

        api_key = os.getenv("THE_COMPANIES_API_KEY")
        if not api_key:
            raise ValueError("The Companies API key is not set. Please set the THE_COMPANIES_API_KEY environment variable.")
        
        # Set the URL and headers
        url = f"https://api.thecompaniesapi.com/v2/companies/{domain}"
        headers = {"Authorization": f"Basic {api_key}"}

        try:
            res = requests.get(url, headers=headers)

            if res.status_code == 404:
                return f"No enrichment data available for company domain '{domain}'"
            
            res.raise_for_status()
            data = res.json()

            about = data.get("about", {})
            location = data.get("locations", {}).get("headquarters", {}).get("address", {}).get("raw", "")
            finances = data.get("finances", {})
            tech_stack = data.get("technologies", {}).get("active", [])[:5]

            return (
                f"Name: {about.get('name')}\n"
                f"Domain: {domain}\n"
                f"Industry: {about.get('industry')}\n"
                f"Employees: {about.get('totalEmployees')}\n"
                f"Revenue: {finances.get('revenue')}\n"
                f"Location: {location}\n"
                f"Tech Stack: {', '.join(tech_stack)}"
            )
        
        except Exception as e:
            return f"Error: {str(e)}"