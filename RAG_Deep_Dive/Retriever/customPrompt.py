import os
from cloudLLM import groq_llm
from dotenv import load_dotenv
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate

load_dotenv()

pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index = os.getenv('PINECONE_INDEX_NAME')

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Initialise LLM
llm = groq_llm

# Initialise Embeddings
embeddings = OllamaEmbeddings(model="llama3:latest")

# Intialise vector store
vector_store = PineconeVectorStore(index_name=pinecone_index, embedding=embeddings)


template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.
Always say "Thanks for asking !" at the end of the answer.
{context}
Question: {question}
Helpful Answer:"""

prompt = PromptTemplate.from_template(template=template)

rag_chain = (
    {"context": vector_store.as_retriever() | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
)

__all__ = [
    rag_chain
]