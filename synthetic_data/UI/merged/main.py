import streamlit as st
import pandas as pd
import json
import os
from synthetic_data import (
    generate_address_for_EU,
    generate_address_for_US,
    read_dataframe_and_generate_data,
)
from synthetic_data import load_data_generation_component, load_template_generation_component, \
    load_data_generation_component_with_faker, extractSchema
from synthetic_data.customer_generation.main import generate_customers
from synthetic_data.order_generation.main import generate_order_data
from synthetic_data.order_line_item_generation.main import (
    generate_order_line_items_data,
)

# Set Session Data
# Initialize session state to preserve data across reruns
if "columns_to_remove" not in st.session_state:
    st.session_state.columns_to_remove = []
if "data_type" not in st.session_state:
    st.session_state.data_type = {}
if "example_data" not in st.session_state:
    st.session_state.example_data = {}
if "foreign_key" not in st.session_state:
    st.session_state.foreign_key = {}
if "new_column" not in st.session_state:
    st.session_state.new_column = {}
# Initialize empty DataFrame
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
# Capture the domains for which the user is generating the template
if "domain" not in st.session_state:
    st.session_state.domain = []
# Capture the OpenAI API key
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""
# Capture the schema extracted from the uploaded CSV
if "schema" not in st.session_state:
    st.session_state.schema = {}

# Set page configuration
st.set_page_config(page_title="Synthetic Data Generator", page_icon="📊", layout="centered")


# Load styles.css for custom styling from assets folder
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("../assets/styles.css")

# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.header("Choose an option")

options = st.sidebar.radio("Select an option", ["Template Generator", "Data Generator", "Data Extractor"])

if options == "Template Generator":
    load_template_generation_component(st)

elif options == "Data Generator":
    # Ask if data needs to be generated using Faker or LLM using a radio button
    data_generation_option = st.radio("Select Data Generation Option", ["Faker", "LLM"])
    if data_generation_option == "LLM":
        # Accept a field for OpenAI API key and the field should be masked
        openai_api_key = st.text_input("Enter OpenAI API Key", type="password")
        if openai_api_key:
            st.session_state.openai_api_key = openai_api_key
            load_data_generation_component(st)
    else:
        load_data_generation_component_with_faker(st)

else:
    extractSchema(st)

