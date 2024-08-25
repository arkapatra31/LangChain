import os
from dotenv import load_dotenv
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from cloudLLM import groq_llm

load_dotenv()

faiss_local_index = os.getenv("FAISS_LOCAL_INDEX_PATH")

llm = groq_llm
embeddings = OllamaEmbeddings(model="llama3:latest")

vector_store = FAISS.load_local(
    folder_path=faiss_local_index, embeddings=embeddings, allow_dangerous_deserialization=True
)

retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

combine_docs_chain = create_stuff_documents_chain(
    llm, retrieval_qa_chat_prompt
)

faiss_retrieval_chain = create_retrieval_chain(
    vector_store.as_retriever(), combine_docs_chain
)

__all__ = [
    faiss_retrieval_chain
]
