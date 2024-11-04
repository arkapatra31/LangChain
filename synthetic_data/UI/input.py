import os
import streamlit as st
from dotenv import load_dotenv
from synthetic_data import get_dataframe_columns
import pandas as pd

load_dotenv()

# Streamlit UI
st.title("Generate Synthetic Data")

# Initialize session state to preserve data across reruns
if 'columns_to_remove' not in st.session_state:
    st.session_state.columns_to_remove = []
if 'data_type' not in st.session_state:
    st.session_state.data_type = {}
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()  # Initialize empty DataFrame

# Input fields
domain = st.text_input("Enter domain of data you are looking for")
number_of = st.number_input("Enter the number of columns:", min_value=1, step=1)

if st.button("Generate Columns"):
    if domain and number_of:
        # Generate columns based on user input
        columns = get_dataframe_columns(domain, number_of)
        st.session_state.df = pd.DataFrame(columns=columns)  # Store DataFrame in session state
        st.success("Dataframe columns generated successfully.")

# Display the DataFrame and its columns if already generated
if st.session_state.df.empty:
    # st.write("### Current DataFrame:")
    # st.dataframe(st.session_state.df)

    for column in st.session_state.df.columns:
        col1, col2, col3 = st.columns([1, 1, 1])

        # Show column name
        col1.write(f"**{column}**")
        # Show dropdown for data type
        data_type = col2.selectbox("Data Type", ["string", "int"], key=f"data_type_{column}")
        st.session_state.data_type[column] = data_type

        # Add a checkbox for removing the column
        remove = col3.checkbox("Remove", key=f"remove_{column}", value=column in st.session_state.columns_to_remove)
        if remove:
            if column not in st.session_state.columns_to_remove:
                st.session_state.columns_to_remove.append(column)
        else:
            if column in st.session_state.columns_to_remove:
                st.session_state.columns_to_remove.remove(column)

    # Button to apply modifications and update the DataFrame
    if st.button("Apply Modifications"):
        # Drop the selected columns
        st.session_state.df.drop(columns=st.session_state.columns_to_remove, inplace=True)
        # Reset the columns_to_remove list after update
        st.session_state.columns_to_remove = []
        st.write("Finalised DataFrame:")
        st.dataframe(st.session_state.df)
        if not os.path.exists("../data"):
            os.mkdir("../data")
        st.session_state.df.to_csv(f"""../data/{domain}.csv""", index=False, mode='w')
