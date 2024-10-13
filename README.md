# Q&A Application using RAG

## Overview 📄
This project provides an end-to-end solution for processing uploaded PDF documents and allowing users to ask questions related to the content using a combination of similarity-based search and a large language model (LLM) response system. The system splits the document into smaller chunks, embeds the text into vector format for similarity search, and then enables users to interactively ask questions. The results come in two parts—retrieved content using similarity search and generated content using an LLM.

## Key Features ✨
- **File Upload**: Users can upload PDF files, which will be processed for further question-answering tasks.
- **Chunking**: The uploaded PDF is split into smaller text chunks for better handling and processing.
- **Embeddings and Similarity Search**: Text chunks are embedded using a model and stored in a vector database (Pinecone), allowing similarity-based search of relevant chunks.
- **Q&A System**: Users can ask questions, and the system will return both retrieved content from the document and generated content using an LLM.
- **Interactive Interface**: The web-based interface allows users to seamlessly interact with the uploaded document and get answers based on both retrieval and generation.

## Project Workflow 🔄
1. **Upload PDF**: The user uploads a PDF document.
2. **Chunking**: The uploaded PDF file is split into smaller text chunks.
3. **Embeddings Generation**: Text chunks are embedded into vector format for storage.
4. **Storing Embeddings**: The embeddings are stored in Pinecone for fast retrieval.
5. **Question Answering**: Users can ask questions based on the uploaded document, and the system retrieves relevant chunks using similarity search and generates additional content using an LLM.

## Project Architecture 🏗️
1. **PDF → Chunks**: The PDF is split into smaller chunks of text.
2. **Embeddings Generation**: Text chunks are embedded into vectors.
3. **Embeddings Storage (Pinecone)**: Vector embeddings are stored in Pinecone for fast retrieval.
4. **Interactive Q&A**: Users can ask questions and receive answers from the embedded data and the LLM.

## Requirements 📋
- Python 3.8 or higher
- Virtual environment management tool (venv, conda, etc.)
- All dependencies listed in `requirements.txt`

## Installation and Setup 🛠️
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and activate a virtual environment**:

   Using `venv`:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

   Using `conda`:
   ```bash
   # Create conda environment
   conda create -n venv python=3.12

   # Activate conda environment
   conda activate venv
   ```

3. **Install dependencies**:
   ```bash
   # Make sure your virtual environment is activated
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

5. **Usage**:
   - Upload a PDF document.
   - Ask questions about the uploaded document through the Q&A interface, and see both retrieved content and generated responses.

## Tech Stack 🛠️
- **Groq**: For LLM-based question generation.
- **Langchain**: For creating modular components and handling text splitting and embeddings.
- **Pinecone**: A vector database for managing embeddings and performing similarity searches.
- **Streamlit**: A web app framework for building the interactive Q&A interface.
- **PyPDF2**: For handling and reading PDF files.

## Troubleshooting 🔍
- **Dependency issues**:
  - Ensure your virtual environment is activated.
  - Verify Python version compatibility: `python --version`.
  - Upgrade `pip` if needed: `pip install --upgrade pip`.
  - If using `conda`, ensure the `conda-forge` channel is added: `conda config --add channels conda-forge`.

## License 📄
The source code for this project is licensed under the MIT License. See the `LICENSE.md` file for more details.

## Contributing 🤝
- Fork the project.
- Create a new feature branch: `git checkout -b feature/AmazingFeature`.
- Commit your changes: `git commit -m 'Add some AmazingFeature'`.
- Push to the branch: `git push origin feature/AmazingFeature`.
- Open a Pull Request.

