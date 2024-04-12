from src.helper import load_pdf, text_split, download_embeddings_model
from langchain_community.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore

load_dotenv()

api_key = os.environ.get("PINECONE_API_KEY")
api_env = os.environ.get("PINECONE_API_ENV")

load_data = load_pdf("Data/")
text_chunks = text_split(load_data)
embeddings = download_embeddings_model()

# Initialize the pinecone
pinecone.Pinecone(api_key=api_key, api_env=api_env)
index_name = "chatbot"

docsearch = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name = "chatbot")