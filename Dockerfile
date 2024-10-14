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

# Set environment variables
ENV GOOGLE_API_KEY=your-google-api-key
ENV PINECONE_API_KEY=your-pinecone-api-key
ENV GROQ_API_KEY=your-groq-api-key

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
