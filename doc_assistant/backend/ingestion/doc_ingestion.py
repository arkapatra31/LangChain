import os

from dotenv import load_dotenv
from pyexpat import features

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import  RecursiveUrlLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


#Method to ingest the doc from the URL and then split it and load into Pinecone index
def ingest_docs():
    # loader = ReadTheDocsLoader("../../langchain-docs")
    loader = RecursiveUrlLoader("https://api.python.langchain.com/en/latest/langchain_api_reference.html")

    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Adding {len(documents)} records to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name=os.getenv('PINECONE_DOCUMENTATION_INDEX')
    )
    print("****Loading to vectorstore done ***")


if __name__ == "__main__":
    ingest_docs()
