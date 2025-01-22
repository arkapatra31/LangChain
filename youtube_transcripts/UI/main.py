from dotenv import load_dotenv
import streamlit as st
from youtube_transcripts import retrieval_chain
from youtube_transcripts.langfuse.callbackHandler import langfuseHandler

# Set page configuration and set page icon to youtube logo
st.set_page_config(page_title="Ask Youtube", page_icon="📹", layout="centered")

st.title("Q&A")

# Input widget for user question
question = st.text_input("Enter your question here")

if question:
    btn = st.button("Ask")
    if btn:
        # Invoke Retrieval Chain using Pinecone as Vector Store with QA prompt from LangChain Hub
        result = retrieval_chain.invoke(
            {
                "input": question
            },
            config={
                "callbacks": [langfuseHandler],
                "run_name": "langfuse-trace-qa",
            }
        )
        st.write(result["answer"])
