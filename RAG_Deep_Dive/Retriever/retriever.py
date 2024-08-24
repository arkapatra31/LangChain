import streamlit as st
from RAG_Deep_Dive.Retriever.createRetrieverChain import retrieval_chain
from RAG_Deep_Dive.Retriever.customPrompt import rag_chain

# Input widget for user question
user_question = st.text_input("Enter your question here")
if user_question:
    # Invoke Retrieval Chain
    result = retrieval_chain.invoke(input={"input": user_question})
    st.subheader("Response from Retrieval Chain")
    st.write(result)

    res = rag_chain.invoke(user_question)
    st.subheader("Response from RAG Chain with Custom Prompt")
    st.write(res)

