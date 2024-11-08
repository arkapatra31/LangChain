import os
import streamlit as st
from dotenv import load_dotenv
from synthetic_data import get_dataframe_columns
import pandas as pd

load_dotenv()

# Streamlit UI
st.title("Generate Records Configuration")

# Initialize session state to preserve data across reruns
if 'columns_to_remove' not in st.session_state:
    st.session_state.columns_to_remove = []
if 'data_type' not in st.session_state:
    st.session_state.data_type = {}
if 'example_data' not in st.session_state:
    st.session_state.example_data = {}
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()  # Initialize empty DataFrame

# Input fields
domain = st.text_input("Enter domain of data you are looking for")
number_of = st.number_input("Enter the number of columns:", min_value=1, max_value=15, step=1)

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
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])

        # Show column name
        col1.write(column)

        if column not in st.session_state.data_type:
            # Set default data type for the column
            st.session_state.data_type[column] = "string"

        # Selectbox to choose data type for the column
        col_type = col2.selectbox(
            "Data Type",
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

        # Show the 4th column to accept example data
        example_data = col4.text_input("Example data", key=f"example_{column}",
                                       placeholder="Enter comma delimited example values")
        st.session_state.example_data[column] = example_data

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
        # st.session_state.df.to_csv(f"""../data/{domain}.csv""", index=False, mode='w')
        configuration = st.session_state.data_type
        final_columns = st.session_state.df.columns.tolist()
        example_data = st.session_state.example_data
        if not os.path.exists("../../config"):
            os.mkdir("../../config")
        # Save data type and example_data against the columns in a JSON format to a single configuration to a file
        with open(f"../../config/{domain}_config.json", "w") as f:
            f.write('{')
            for column in final_columns:
                #Split the example data by comma and strip whitespaces
                examples = [example.strip() for example in example_data[column].split(",") if example] if example_data[column] else []
                f.write(f'"{column}": {{"data_type": "{configuration[column]}", "example_data": "{examples}"}}')
                if column != final_columns[-1]:
                    f.write(", ")
            f.write('}')
        f.close()
        st.success(f"Data saved as {domain}_config.json")
