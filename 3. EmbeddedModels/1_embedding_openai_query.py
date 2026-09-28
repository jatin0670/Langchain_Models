from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of india")


print(str(result))


#this code will create a embedding thing from text (basically it creates cordinates or vectors according to the context of input)