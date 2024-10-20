from crewai import Task
from textwrap import dedent


class Custom_Tasks():

    def __init__(self,query):
        self.query=query

    def __tip_section(self):
        return "If you do a good job, you will get a big reward"

    def answer(self,agent,tools):
        return Task(
            description=dedent(f"""
            **Task**: Get answer the question of the user.
            **Description**: Answer the user's question with the utmost precision and prevent any personal biases.
            **Parameters**: {self.query}
            **Tip**:{self.__tip_section()}
            """
            ),
            expected_output="A 4 paragraph answer to the question, {self.query} ",
            tools=[tools],
            agent=agent
        )