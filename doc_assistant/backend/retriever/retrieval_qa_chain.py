import os
from dotenv import load_dotenv
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone

load_dotenv()

INDEX_NAME = os.getenv('PINECONE_DOCUMENTATION_INDEX')


def run_llm(query: str):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)

    chat_llm = ChatOpenAI(model="gpt-4o-mini", verbose=True, temperature=0)

    retrieval_qa_chain = RetrievalQA.from_chain_type(
        llm=chat_llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )

    return retrieval_qa_chain.invoke({"query": query})


if __name__ == "__main__":
    response = run_llm(query="What is Retrieval QA Chain ?")
    print(response)
