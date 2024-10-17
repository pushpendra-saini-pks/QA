# app/Dockerfile

FROM python:3.12

COPY . /app

COPY requirements.txt ./requirements.txt

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

# Set environment variables
ENV GOOGLE_API_KEY=your_google_api_key 
ENV PINECONE_API_KEY=your_pincone_api_key 
ENV GROQ_API_KEY=your_groq_api_key

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py"]
CMD ["streamlit", "run", "app.py"]
