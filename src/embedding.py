from langchain_pinecone import PineconeVectorStore
from langchain.docstore.document import Document 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# initialize the embeddings model 
doc_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
    
)

# pinecone setup 
index_name = "test1"

def store_embeddings(document_chunks):
    docsearch = PineconeVectorStore.from_documents(document_chunks,doc_embeddings,index_name=index_name)
    return docsearch