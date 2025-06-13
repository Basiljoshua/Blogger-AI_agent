from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERVER_API_KEY']=os.getenv('SERVER_API_KEY')

from crewai_tools import SerperDevTool

#initialize the tool for internet searching capabilitiies 
tool= SerperDevTool()