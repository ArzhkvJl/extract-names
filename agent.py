from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field
import spacy
from pathlib import Path
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
import json


class InfoResponse(BaseModel):
    """Give the response containing this information"""
    name: str = Field(description="Company name")
    website: str = Field(description="Company website URL")
    sector: str = Field(description="Industry sector the company operates in")
    location: str = Field(description="Company headquarters location")
    description: str = Field(description="One-sentence description")
    people: str = Field(
        description="The most important people in the company like CEO, founders"
    )
    analysis: str = Field(
        description="A brief analysis (max 2 sentences) of the company in comparison with a couple of main competitors."
                    "Mention the competitors"
    )


def companies(num: str) -> set:
    """Extract company names from the input text"""
    nlp = spacy.load("en_core_web_trf")
    # nlp = spacy.load("ru_core_news_lg")

    content = json.loads(Path("input.json").read_text())[num]
    doc = nlp(content)
    company_names = set()
    for ent in doc.ents:
        should_add = True
        if ent.label_ == "ORG":
            for company in company_names:
                if ent.text in company:
                    should_add = False
                    break
            if should_add:
                company_names.add(ent.text)
    return company_names


def create_agent():
    model = ChatGroq(
        model="llama-3.3-70b-versatile", temperature=0.7,)

    tool = TavilySearchResults(max_results=6)
    agent = create_react_agent(
        model=model,
        tools=[tool],
        response_format=InfoResponse,
        prompt="You are a helpful assistant who uses web search to provide structured information about companies."

    )
    return agent




