#simple LLM Code but we dont use llms now, we use ChatModels  

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()   #this imports the api key from .evn file (but we dont have openAI api cause its paid)

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("what is the capital of india")

print(result)