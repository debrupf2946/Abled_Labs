from crewai import Task
from textwrap import dedent

class  news_anlysis_task:
    def news_retriever(self,agent,func):
        return Task(description=dedent(""""""),
                agent=agent

        )
    def Analyse(self,agent):
        return Task(description=dedent(""""""),agent=agent)
    def news_summariser(self,agent):
        return Task(description=dedent(""""""),agent=agent)
    def chat(self,agent):
        return Task(description=dedent(),agent=agent)


