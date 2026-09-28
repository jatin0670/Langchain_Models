from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "delhi is the capital of india",
    "kolkata is the capitak of west bengal",
    "paris is the capital of france"
]

result = embedding.embed_documents(documents)


print(str(result))


#this is used to generate cordinates from list of somthing(documents)