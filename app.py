import os 
import streamlit as st 
from dotenv import load_dotenv
from groq import Groq
from src.chunk1 import chunking
from src.embedding import store_embeddings
from src.question_answer import query_vector_database, transcript_chat_completion
from langchain.docstore.document import Document

# Load the environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Ensure the api_key is loaded 
if API_KEY is None:
    st.error("API KEY not found. Please set the Groq API key in your .env file.")
    st.stop()

# Initialize the Groq client 
client = Groq(api_key=API_KEY)

# Ensure output directories exist 
file_folder = "uploaded_file"
chunk_folder = "chunks"

os.makedirs(file_folder, exist_ok=True)
os.makedirs(chunk_folder, exist_ok=True)


st.set_page_config(layout="wide")  # full page 


# Full-width container for title, file uploader, and text input
st.title("Q&A Application using RAG")  # Title spans full width

# Full-width file uploader 
uploaded_file = st.file_uploader("Upload a file", type="pdf")  # File uploader spans full width

# Full-width text input for the question
user_question = st.text_input("Ask a question about your uploaded document")  # Input spans full width

# Session state to store the last processed file to avoid reprocessing 
if "last_uploaded_file" not in st.session_state:
    st.session_state.last_uploaded_file = None

if "chunk" not in st.session_state:
    st.session_state.chunk = []

if "docsearch" not in st.session_state:
    st.session_state.docsearch = None

# When a new file is uploaded, reset the session state for transcriptions and embeddings 
if uploaded_file is not None:
    # Check if the new file is different from the last processed files 
    if uploaded_file.name != st.session_state.last_uploaded_file:
        st.session_state.chunk = []
        st.session_state.docsearch = None
        st.session_state.last_uploaded_file = uploaded_file.name
        
    # Save the uploaded file 
    filepath = os.path.join(chunk_folder, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    # Chunking 
    if not st.session_state.chunk:
        documents = chunking(filepath)
        
        # Embedding and docstore 
        st.session_state.docsearch = store_embeddings(documents)

# # Ask a question about the uploaded document
# user_question = st.text_input("Ask a question about your uploaded document")

if user_question and st.session_state.docsearch:
    # Retrieve content using similarity search
    relevant_transcripts = query_vector_database(st.session_state.docsearch, user_question)
    
    # Generate content using LLM
    response = transcript_chat_completion(client, relevant_transcripts, user_question)
    
    # Layout: divide the full page into two equal halves
    col1, col2 = st.columns([1, 1])  # 1:1 ratio for equal width
    
    # Show the LLM-generated content in the first column (left half)
    with col1:
        st.subheader("✅ Generated Content by LLM")
        st.write(response)
    
    # Show the retrieved content by similarity search in the second column (right half)
    with col2:
        st.subheader("👍Retrieved Content by Similarity Search")
        for i, transcript in enumerate(relevant_transcripts, 1):
            st.write(f"**Document** {i}: {transcript}")
