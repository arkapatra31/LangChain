import os

import streamlit as st
from dotenv import load_dotenv
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from cloudLLM import groq_llm
from langchain_pinecone import PineconeVectorStore

load_dotenv()

pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index = os.getenv('PINECONE_INDEX_NAME')

# Input widget for user question
user_question = st.text_input("Enter your question here")
if user_question:
    # Initialise LLM
    llm = groq_llm

    # Initialise Embeddings
    embeddings = OllamaEmbeddings(model="llama3:latest")

    # Intialise vector store
    vector_store = PineconeVectorStore(index_name=pinecone_index, embedding=embeddings)

    # Pull the prompt for qa-chain from LangChain Hub
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    # Create the chain of type document stuff
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

    # Create the Retrieval Chain
    retrieval_chain = create_retrieval_chain(
        retriever=vector_store.as_retriever(), combine_docs_chain=combine_docs_chain
    )
    result = retrieval_chain.invoke(input={"input": user_question})
    st.write(result)
