
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


# Data extract fro all pdf stored in Data directory
def load_pdf(data):
    loader  = DirectoryLoader(data,
                              glob = "*pdf*",
                              loader_csl = PyPDFLoader)
    documents = loader.load()

    return documents


# create chunks of text
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(extracted_data, chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Download embedding models
def download_embeddings_model():
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    return embeddings