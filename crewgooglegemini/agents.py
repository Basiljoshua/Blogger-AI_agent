from crewai import Agent
from tools import tool

from dotenv import load_dotenv
# to load all environment variables
load_dotenv()

import os;

from langchain_google_genai import ChatGoogleGenerativeAI
## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemma-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY")
                           )

#creating a senior researcher agent with memory and verbose mode
news_researcher=Agent(
    role="Senior Researcher",
    goal="Uncover goundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you are at the forefont of"
        "innovation, eager to explore and share knowledge that could"
        "change the world"
    ),
    tools=[tool],
    llm=llm, #by default it uses openai llm model
    allow_delegation=True
)

# Creating a writer agent with custom tools responsible for writing news blog
news_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner "
    ),
    tools=[tool],
    llm=llm, #by default it uses openai llm model
    allow_delegation=False
)