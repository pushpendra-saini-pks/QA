from groq import Groq
### llm model 
def transcript_chat_completion(client, relevant_docs, user_question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":'''use this relevant_docs  to answer any user questions,citing specific quotes:
                {relevant_docs}
                '''.format(relevant_docs=relevant_docs)
            },
            {
                "role":"user",
                "content":user_question,
            }
        ],
        model="llama3-8b-8192",
        
    )
    return chat_completion.choices[0].message.content


### retrieval by similarity search 
def query_vector_database(docsearch,user_query):
    relevant_docs = docsearch.similarity_search(user_query)
    return [doc.page_content for doc in relevant_docs[:3]]
