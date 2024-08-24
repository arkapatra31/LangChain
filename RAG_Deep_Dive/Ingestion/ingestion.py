import os
import streamlit as st
from dotenv import load_dotenv
from cloudLLM import groq_llm
from langchain_pinecone import PineconeVectorStore
from RAG_Deep_Dive.utils.chunkifyData import convert_text_to_chunks

load_dotenv()
pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index = os.getenv('PINECONE_INDEX_NAME')


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


if __name__ == "__main__":
    # Use Streamlit to create a minimalistic UI for the file uploading
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

        # Initialise vector DB
        vector_store = PineconeVectorStore.from_texts(texts=chunks, index_name=pinecone_index, embedding=embeddings)

        if vector_store:
            print("Vector Store Created")
