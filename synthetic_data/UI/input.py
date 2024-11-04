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

# Button to generate columns
if st.button("Generate Columns"):
    if domain and number_of:
        # Generate columns based on user input
        columns = get_dataframe_columns(domain, number_of)
        st.session_state.df = pd.DataFrame(columns=columns)  # Store DataFrame in session state
        st.success("Dataframe columns generated successfully.")

# Show the generated DataFrame
if st.session_state.df.empty:
    for column in st.session_state.df.columns:
        col1, col2, col3 = st.columns([1, 1, 1])

        # Show column name
        col1.write(f"**{column}**")

        if column not in st.session_state.data_type:
            # Set default data type for the column
            st.session_state.data_type[column] = "string"

        # Selectbox to choose data type for the column
        col_type = col2.selectbox(
            f"Select data type for {column}",
            ["string", "int"],
            key=f"type_{column}",
            index=["string", "int"].index(st.session_state.data_type[column])
        )

        # Update the data type in session state
        st.session_state.df[column] = st.session_state.df[column].astype(col_type)
        st.session_state.data_type[column] = col_type

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
        # if not os.path.exists("../data"):
        #     os.mkdir("../data")
        #st.session_state.df.to_csv(f"""../data/{domain}.csv""", index=False, mode='w')
        configuration = st.session_state.data_type
        final_columns = st.session_state.df.columns.tolist()
        if not os.path.exists("../data"):
            os.mkdir("../data")
        with open(f"../data/{domain}.json", "w") as f:
            f.write("{")
            for column in final_columns:
                f.write(f'"{column}": "{configuration[column]}",')
            f.write("}")
        f.close()

