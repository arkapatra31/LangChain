import random
from typing import Set
from doc_assistant.backend.retriever.retriever import run_llm
import streamlit as st
from streamlit_chat import message

st.header("Documentation Assistant")

prompt = st.text_input("Prompt", placeholder="Enter your prompt here")

if (
        "chat_answers_history" not in st.session_state
        and "user_prompt_history" not in st.session_state
        and "chat_history" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []


def create_sources_string(sources: Set[str]) -> str:
    if sources is None:
        return ""
    else:
        source_string = "Sources: \n"
        sources = list(sources)
        for i, source in enumerate(sources):
            source_string += f"{i + 1}. {source}\n"
        return source_string


if prompt:
    with st.spinner("Generating Response...."):
        response = run_llm(query=prompt, chat_history=st.session_state["chat_history"])
        sources = set([doc.metadata["source"] for doc in response["context"]])

        formatted_response = f"{response["answer"]} \n \n {create_sources_string(sources)}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", response["answer"]))

if st.session_state["chat_answers_history"] is not None:
    if st.session_state["chat_answers_history"]:
        for generated_response, user_query in zip(
                st.session_state["chat_answers_history"],
                st.session_state["user_prompt_history"],
        ):
            message(user_query, is_user=True, key=random.randint(0, 99999))
            message(generated_response, key=random.randint(0, 99999))
