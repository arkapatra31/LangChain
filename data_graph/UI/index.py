import streamlit as st
from data_graph import createGraph
from dotenv import load_dotenv

load_dotenv()

st.title("Data Graph")

uploaded_files = st.file_uploader("Upload CSV files", type="csv", accept_multiple_files=True)

if uploaded_files:
    generate_btn = st.button("Generate Cypher Query")
    if generate_btn:
        input_data = []
        for file in uploaded_files:
            input_data.append(file.getvalue().decode("utf-8"))
        output = createGraph(input_data)
        st.write(output)
