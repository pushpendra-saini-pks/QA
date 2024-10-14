# app/Dockerfile

FROM python:3.12

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

# Set environment variable 
ENV os.environment["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

ENV os.environment["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")

ENV os.environment["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
