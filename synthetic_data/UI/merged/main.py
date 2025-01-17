import streamlit as st
import pandas as pd
import json
import os
from synthetic_data import (
    generate_address_for_EU,
    generate_address_for_US,
    read_dataframe_and_generate_data,
)
from synthetic_data import load_data_generation_component, load_template_generation_component
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

options = st.sidebar.radio("Select an option", ["Template Generator", "Data Generator"])

if options == "Template Generator":
    load_template_generation_component(st)
else:
    load_data_generation_component(st)
