import os
from dotenv import load_dotenv
from crewai import Agent,LLM
from crewai_tools import PDFSearchTool

load_dotenv()
    

class Custom_Agents:

    def __init__(self):
        self.llm=LLM(model="gemini/gemini-1.5-flash",api_key=os.getenv("GOOGLE_API_KEY"))
    
    def detailedembed(self):
        self.textsearcher=PDFSearchTool(pdf="./Jungle_Book_Big.pdf",
                                        config=dict(
                                            llm=dict(config=dict(model="gemini-1.5-flash")),
                                            embedder=dict(provider="google",config=dict(model="models/embedding-001"))
                                        ))

    def weakembed(self):
        self.smalltextsearcher=PDFSearchTool(pdf="./The-Jungle-Books-text.pdf",
                                             config=dict(
                                            llm=dict(config=dict(model="gemini-1.5-flash")),
                                            embedder=dict(provider="google",config=dict(model="models/embedding-001"))
                                        ))

    def detailed_book_agent(self):
        return Agent(
            role="Literary Expert",
            backstory="I am a professional literary expert. I have read thousands of books and my knowledge knows no bounds. I can read a book a single time and know all there is to it",
            goal="Read the given book and answer the question asked in a detailed and thorough manner. ONLY give the answer from the pdf",
            verbose=True,
            allow_delegation=False,
            tools=[self.textsearcher],
            llm=self.llm
        )
    
    def short_book_agent(self):
        return Agent(
            role="Literary Scholar",
            backstory="I am an enthusiastic literary scholar. I have read hundreds of books and my learning rate is very high. I can read a book a single time and give factually correct answers",
            goal="Read the given book and answer the question asked in a simple manner. ONLY give the answer from the pdf",
            verbose=True,
            allow_delegation=False,
            tools=[self.smalltextsearcher],
            llm=self.llm
        )

