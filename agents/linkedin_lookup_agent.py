import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)



def lookup(name):

    llm = Ollama(model="gemma:2b")

    template = """given the full name {name_of_person} I want
                    you to get me a link to their Linkedin profile page.
                    Your answer should contain only a URL"""    

    prompt_template = PromptTemplate(input_variables=['name_of_person'], template= template)

    
    return 