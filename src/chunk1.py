# chunk.py
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document # Import the Document schema
from langchain.docstore.document import Document 

def chunking(filepath):
    # Load the PDF document using LangChain's PyPDFLoader
    loader = PyPDFLoader(filepath)
    documents = loader.load()

    # Extract text content from each Document object
    full_text = " ".join([doc.page_content for doc in documents])

    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Split the concatenated string into chunks
    document_chunks = text_splitter.split_text(full_text)

    # Handle encoding issues if needed
    document_chunks = [chunk.encode('utf-8', 'ignore').decode('utf-8') for chunk in document_chunks]

    # Wrap each text chunk into a Document object
    document_objects = [Document(page_content=chunk) for chunk in document_chunks]

    return document_objects
