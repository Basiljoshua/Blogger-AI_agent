from crewai import Crew,Process
from agents import news_researcher,news_writer
from tasks import write_task,research_task

## Forming the tech focussed crew with sequential process type
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task,],
    process=Process.sequential,

)

## Starting the tasks execution with enhances feedback
result = crew.kickoff(inputs={'Topic - AI in healthcare'})
print(result)