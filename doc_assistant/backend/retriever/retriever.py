import os
from typing import List, Dict, Any

from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

INDEX_NAME = os.getenv('PINECONE_DOCUMENTATION_INDEX')


def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
    chat_llm = ChatOpenAI(model="gpt-4o-mini", verbose=True, temperature=0)

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_documents_chain = create_stuff_documents_chain(chat_llm, retrieval_qa_chat_prompt)

    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    history_aware_retriever = create_history_aware_retriever(
        llm=chat_llm, retriever=vector_store.as_retriever(), prompt=rephrase_prompt
    )

    # retriever_chain = create_retrieval_chain(retriever=vector_store.as_retriever(),
    #                                          combine_docs_chain=stuff_documents_chain)

    '''history_aware_retriever to replace vector store as retriever while using rephrase prompting'''
    retriever_chain = create_retrieval_chain(retriever=history_aware_retriever,
                                             combine_docs_chain=stuff_documents_chain)

    result = retriever_chain.invoke(input={
        "input": query,
        "chat_history": chat_history
    })
    return result


if __name__ == "__main__":
    response = run_llm(query="Langchain Language Models")
    print(response['answer'])

__all__ = [
    run_llm
]
