#CREATE A .env FILE AND ENTER YOUR GOOGLE_API_KEY

from crewai import Crew,Process
from textwrap import dedent
from customagents import Custom_Agents
from customtasks import Custom_Tasks

class Custom_Crew:
    def __init__(self,condition):
        self.medicalcondition=condition
        pass

    def run(self):
        
        custom_agents=Custom_Agents()
        custom_tasks=Custom_Tasks()

        validitybot=custom_agents.validitychecker()
        detailsbot=custom_agents.detailsprovider()
        treatmentbot=custom_agents.treatmentprovider()

        validitycheck=custom_tasks.check_valid_treatment(validitybot,self.medicalcondition)
        detailscheck=custom_tasks.condition_details(detailsbot,self.medicalcondition)
        treatmentcheck=custom_tasks.treatment_details(treatmentbot,self.medicalcondition)


        crew=Crew(
            agents=[validitybot,detailsbot,treatmentbot],
            tasks=[validitycheck,detailscheck,treatmentcheck],
            verbose=True,
            process=Process.sequential
        )

        result=crew.kickoff()

        return result
    
if __name__=="__main__":

    while (True):
        print("Enter a Medical Condition to learn about: (type exit to quit)")
        user_input=input(">")
        if(user_input=="exit"):
            break
        medcrew=Custom_Crew(user_input)
        result=medcrew.run()
        print(result)

