from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions = 300)

documents = [
    "Virat Kohli is former India captain",
    "Steve Smith is formar Australia captain",
    "Shubhman Gill is number 1 ODI batter",
    "Jasprit Bumrah is world number 1 bowler"
]

query = 'Tell me about Virat Kohli'

doc_embedding = embeddinig.embed_documents(documents)

embed_query = embedding.embed_query(query)

scores = cosine_similarity([embed_query],doc_embedding)

index,score = sorted(list(enumerate(scores)),key = lambda x: x[1])[-1]