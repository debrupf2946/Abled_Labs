import os
from textwrap import dedent
from crewai import Agent
from langchain.agents import load_tools
from langchain.llms import genai
from langchain_google_genai import GoogleGenerativeAI


llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=key)




class Voice_news_assistant:
    def __init__(self):
        self.llm=llm
    def news_fetcher(self):
        return Agent(
            role="Lead NEWS retriever",
            goal=dedent("""
            """),
            backstory=dedent("""
            """),
            tools=[],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    def news_analyser(self):
        return Agent(
            role="Cheif NEWS edditor",
            goal=dedent("""
            """),
            backstory=dedent("""
            """),
            tools=[],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    def news_Reporter(self):
        return Agent(
            role="Principal News Reporter",
            goal=dedent("""
            """),
            backstory=dedent("""
            """),
            tools=[],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

