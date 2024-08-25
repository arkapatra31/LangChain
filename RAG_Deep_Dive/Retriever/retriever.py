import streamlit as st
from RAG_Deep_Dive.Local_Vector_Store.faiss_vector_store import faiss_retrieval_chain
from RAG_Deep_Dive.Retriever.createRetrieverChain import retrieval_chain
from RAG_Deep_Dive.Retriever.customPrompt import rag_chain

# Input widget for user question
st.header("Q&A")
user_choice = st.text_input(
    """
    Which of the following you wish to use?\n
    1.Pinecone Retriever with LangSmith provided QA Chat Prompt\n
    2. Pinecone Retriever with Custom Prompt\n
    3. FAISS as Retriever
    """
)

user_question = st.text_input("Enter your question here")
if user_question:
    st.subheader("*****RESPONSE*****")
    if user_choice == "1":
        # Invoke Retrieval Chain using Pinecone as Vector Store with QA prompt from LangChain Hub
        result = retrieval_chain.invoke(input={"input": user_question})
        st.write(result)

    elif user_choice == "2":
        # Invoke Retrieval Chain using Pinecone as Vector Store with custom prompt
        result = rag_chain.invoke(user_question)
        st.write(result)

    elif user_choice == "3":
        # Invoke Retrieval Chain using FAISS Local Vector Store
        result = faiss_retrieval_chain.invoke({"input": user_question});
        st.write(result)

    else:
        st.write("INVALID OPTION SELECTION")
        print("Invalid Choice")
