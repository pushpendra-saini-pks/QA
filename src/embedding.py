# from langchain_pinecone.vectorstores import Pinecone
# # from langchain.docstore.document import Document 
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# # initialize the embeddings model 
# doc_embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/text-embedding-004"
    
# )

# # pinecone setup 
# index_name = "test1"

# def store_embeddings(document_chunks):
#     docsearch = Pinecone.from_documents(document_chunks,doc_embeddings,index_name=index_name)
#     return docsearch


from langchain_pinecone.vectorstores import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings

index_name = "test1"

def store_embeddings(document_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )

    docsearch = Pinecone.from_documents(
        documents=document_chunks,
        embedding=embeddings,
        index_name=index_name
    )
    return docsearch
