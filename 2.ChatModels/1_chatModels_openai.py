# same as a 1_llm_demo

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI('gpt-4')

result = model.invoke("what is the capital of india")

print(result.content) #this result gives so many thing but the actual answer lies in the content section