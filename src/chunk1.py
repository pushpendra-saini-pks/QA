# chunk.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunking(filepath):
    # Load the PDF document using LangChain's PyPDFLoader
    loader = PyPDFLoader(filepath)
    documents = loader.load()

    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Split the documents into chunks
    documents = text_splitter.split_documents(documents)

    return documents