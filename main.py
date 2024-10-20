#CREATE A .env FILE AND MAKE A GOOGLE_API_KEY VARIABLE WITH YOUR GOOGLE AI KEY

from customagents import Custom_Agents
from customtasks import Custom_Tasks
from crewai import Crew

customagents=Custom_Agents()

class Custom_Crew():
    def __init__(self,query):
        self.query=query
    
    def run(self):
        
        customtasks=Custom_Tasks(query=self.query)

        ProfessionalAgent=customagents.detailed_book_agent()
        AmateurAgent=customagents.short_book_agent()

        HeavyReadingTask=customtasks.answer(agent=ProfessionalAgent,tools=customagents.textsearcher)
        LightReadingTask=customtasks.answer(agent=AmateurAgent,tools=customagents.smalltextsearcher)

        readingcrew=Crew(
            agents=[ProfessionalAgent,AmateurAgent],
            tasks=[HeavyReadingTask,LightReadingTask],
            verbose=True
        )
        
        result=readingcrew.kickoff()
        return result




if __name__=="__main__":
    print("READING COMMENCING")

    customagents.weakembed()
    customagents.detailedembed()

    
    while(True):
        print("Enter a Question about the book (""Exit"" to Leave)")
        user_input=input(">")
        
        if(user_input=="Exit"):
            break

        crew=Custom_Crew(query=user_input)
        result=crew.run()

        print(result)
