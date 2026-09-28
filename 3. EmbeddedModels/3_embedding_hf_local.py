from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "delhi is the capital of india"

documents = [
    "delhi is the capital of india",
    "kolkata is the capitak of west bengal",
    "paris is the capital of france"
]

vector = embedding.embed_query(text)

vectorDoc = embedding.embed_documents(documents)

print(str(vector))

print(str(vectorDoc))



#this code will first donwload the embedding model into your system then convert the text or documents into vector or cordinates