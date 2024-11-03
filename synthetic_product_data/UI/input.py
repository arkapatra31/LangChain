import os
import streamlit as st
from dotenv import load_dotenv
from synthetic_product_data import get_dataframe_columns
import pandas as pd

load_dotenv()

# Streamlit UI
st.title("Generate Synthetic Data")

# Input fields
domain = st.text_input("Enter domain of data you are looking for")
number_of = st.number_input("Enter the number of columns:", min_value=1, step=1)

if st.button("Generate Columns"):
    if domain and number_of:
        columns = get_dataframe_columns(domain, number_of)
        df = pd.DataFrame(columns=columns)
        file_name = f"""{domain}.csv"""
        df.to_csv(path_or_buf=f"""../data/{file_name}""", index=False)
        st.success("Dataframe columns generated successfully.")
    else:
        st.error("Please provide both domain details and number of columns.")