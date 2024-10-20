import os
from dotenv import load_dotenv
from crewai import Agent,LLM
from textwrap import dedent

load_dotenv()

class Custom_Agents:
    def __init__(self):
        self.llm=LLM(model="gemini/gemini-1.5-flash",api_key=os.getenv("GOOGLE_API_KEY"))

    def validitychecker(self):
        return Agent(
            role="Professional Medical Condition Validity Checker",
            backstory=dedent(f"""Medical Expert.
                             I have years of practice in recognizing medical conditions"""),
            goal=dedent(f"""Check if the provided medical condition exists or not. ONLY check the validity and nothing else. """),
            tools=[],
            verbose=False,
            allow_delegation=False,
            llm=self.llm,
        )

    def detailsprovider(self):
        return Agent(
            role="Professional Medical Expert",
            backstory=dedent(f"""Medical Expert.
                             I have years of practice in explaining medical conditions. I do not know anything else"""),
            goal=dedent(f"""Give a detailed description about the medical condition. Do NOT provide any information about treatments"""),
            tools=[],
            verbose=False,
            allow_delegation=False,
            llm=self.llm,
        )
    
    def treatmentprovider(self):
        return Agent(
            role="Professional Medical Treatment Expert",
            backstory=dedent(f"""Medical Expert.
                             I have years of practice in treating medical conditions. I do not know anything else"""),
            goal=dedent(f"""Give a detailed treatment about the medical condition.Also provide a link to a website covering the medical condition. ONLY provide reputed and scientifically backed websites"""),
            tools=[],
            allow_delegation=False,
            llm=self.llm,
        )

