import streamlit as st
import pandas as pd
from data_graph import createGraphConfiguration, create_cypher_query
from dotenv import load_dotenv
import json

from streamlit import session_state

load_dotenv()


st.title("Data Graph")

uploaded_files = st.file_uploader("Upload CSV files", type="csv", accept_multiple_files=True)

if uploaded_files:
    generate_btn = st.button("Generate Graph Configuration")
    if generate_btn:
        input_data = []
        for file in uploaded_files:
            input_data.append(file.getvalue().decode("utf-8"))
        output = createGraphConfiguration(input_data)
        st.write(output)
        cypher_query = create_cypher_query(uploaded_files, output)
        st.write(cypher_query)
