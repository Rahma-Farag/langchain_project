import os 
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
# from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("langchain")
    # print(os.environ['OPENAI_API_KEY'])


    summary_template ="""
    given the infromation {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    

    summary_prompt_template = PromptTemplate(input_variables=['information'], template= summary_template)

    # llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    llm = Ollama(model="gemma:2b")
    # result = llm.invoke("The first man on the moon was ...")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url= 'https://gist.githubusercontent.com/Rahma-Farag/2a933b5d3d08b366cce809c7d516be6b/raw/447399dab0b3bbc0c82c3404fe889079c9df9fdd/rahma-farag.json', 
        mock= True
    )
    raw_result = chain.invoke(input={"information": linkedin_data})
    # raw_result = chain.run({"information": information})
    result = (list(raw_result.items())[1])[1]
    print(result)