import os
from builtins import int
from typing import Any
import streamlit as st
from dotenv import load_dotenv
from cloudLLM import groq_llm
from langchain_community.embeddings import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import FAISS
from RAG_Deep_Dive.utils.chunkifyData import convert_text_to_chunks
from RAG_Deep_Dive.utils.pdfToText import extract_text_from_pdf

load_dotenv()
pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index = os.getenv('PINECONE_INDEX_NAME')
faiss_local_index = os.getenv("FAISS_LOCAL_INDEX_PATH")

if __name__ == "__main__":
    # Use Streamlit to create a minimalistic UI for the file uploading
    # Select Target Vector Store from User
    target_vector_store = st.text_input("""
    Choose Target Vector Store from the below options :\n
    1. Pinecone
    2. FAISS
    """)

    st.title("Upload Documents to be embedded")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(uploaded_file)

        # Convert text to chunks
        chunks = convert_text_to_chunks(text)

        # Create embeddings
        embeddings = OllamaEmbeddings(model="llama3:latest")

        # Instantiate LLM
        llm = groq_llm

        vector_store: Any
        if target_vector_store == "1":
            # Initialise and load embedded documents to Pinecone Vector Store
            vector_store: PineconeVectorStore = PineconeVectorStore.from_texts(
                texts=chunks, index_name=pinecone_index,
                embedding=embeddings)
        elif target_vector_store == "2":
            # Initialise and load embedded documents to FAISS Local Vector Store
            vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
            vector_store.save_local(faiss_local_index)
        else:
            raise ValueError("Invalid Selection")

        if isinstance(vector_store, PineconeVectorStore):
            st.write("Pinecone Vector Store Created")
        else:
            st.write("FAISS Local Vector Store Created")
