from langchain_pinecone import PineconeVectorStore
from langchain.docstore.document import Document 
from langchain_google_genai import GoogleGenerativeAIEmbeddings

doc_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
    
)


index_name = "test1"

def store_embeddings(chunks):
    docsearch = PineconeVectorStore.from_documents(chunks,doc_embeddings,index_name=index_name)
    return docsearch