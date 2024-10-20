from crewai import Task
from textwrap import dedent

class Custom_Tasks:
    def __tip_section(self):
        return "If you do well, you will be provided 500 rupees!!"
    
    def check_valid_treatment(self,agent,condition):
        return Task(
            description=dedent(f"""
            **Task**: Check if the given condition is valid
                               
            **Description**:Thoroughly check and confirm if the given condition actually exists. ONLY use sources of data that are reputable
            
            **Parameters**:
            -Condition:{condition}

            **Note**: {self.__tip_section()}
            """),
            
            expected_output="A 1 line statement on whether {condition} exists or not",
            agent=agent
        )
    
    def condition_details(self,agent,condition):
        return Task(
            description=dedent(f"""
            **Task**: Get the condition details for the given condition
                               
            **Description**: Give a detailed and in-depth explanation of the condition, its symptoms, and some of the causes of the condition. DO NOT give the treatment.
            
            **Parameters**:
            -Condition:{condition}

            **Note**: {self.__tip_section()}
            """),

            expected_output="A 4 paragraph description of the {condition}, barring the treatment",
            agent=agent
        )
    
    def treatment_details(self,agent,condition):
        return Task(
            description=dedent(f"""
            **Task**: Get the treatment details for the given condition
                               
            **Description**: Give a detailed and in-depth explanation of the treatment of the condition. DO NOT recommend experimental or inhumane treatments.
            
            **Parameters**:
            -Condition:{condition}

            **Note**: {self.__tip_section()}
            """),

            expected_output="A 2 paragraph description of the {condition}",
            agent=agent
        )