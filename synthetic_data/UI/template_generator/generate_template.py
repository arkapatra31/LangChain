import os
import streamlit as st
from dotenv import load_dotenv
from synthetic_data import get_dataframe_columns
import pandas as pd

load_dotenv()

def load_template_generation_component(st):

    # Streamlit UI
    st.title("Template Generator")
    st.write("Create a realtime template or schema for your data and customise it as per your requirements.")

    # Input fields
    domain: str = st.text_input("Enter domain of data you are looking for")
    number_of = st.number_input(
        "Enter the number of columns:", min_value=5, max_value=15, step=1
    )

    # Button to generate columns
    if st.button("Generate Columns"):
        with st.spinner("Generating columns..."):
            if domain and number_of:
                # Generate columns based on user input
                columns = get_dataframe_columns(domain.replace(" ", "_"), number_of)
                st.session_state.df = pd.DataFrame(
                    columns=columns
                )  # Store DataFrame in session state
                st.success("Dataframe columns generated successfully.")

    # Show the generated DataFrame
    if st.session_state.df.empty:
        for column in st.session_state.df.columns:
            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 2.5, 1])

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
                index=["string", "int"].index(st.session_state.data_type[column]),
            )

            # Update the data type in session state
            st.session_state.df[column] = st.session_state.df[column].astype(col_type)
            st.session_state.data_type[column] = col_type

            # Add a checkbox for removing the column
            remove = col3.checkbox(
                "Remove",
                key=f"remove_{column}",
                value=column in st.session_state.columns_to_remove,
            )
            if remove:
                if column not in st.session_state.columns_to_remove:
                    st.session_state.columns_to_remove.append(column)
            else:
                if column in st.session_state.columns_to_remove:
                    st.session_state.columns_to_remove.remove(column)

            # Show the 4th column to accept example data
            example_data = col4.text_input(
                "Example data",
                key=f"example_{column}",
                placeholder="Enter comma delimited example values",
            )
            st.session_state.example_data[column] = example_data

            # Mark where the field can be used as foreign key
            is_foreign_key = col5.checkbox("Foreign Key", key=f"foreign_key_{column}")
            if is_foreign_key:
                st.session_state.foreign_key[column] = 1
            else:
                st.session_state.foreign_key[column] = 0


    def add_column():
        # Create a form to take input for column name, datatype from dropdown and example data
        if st.checkbox("Add Columns"):
            with st.form(key="add_columns"):
                new_column = st.text_input("Column Name")
                st.session_state.new_column["name"] = new_column
                new_column_type = st.selectbox("Data Type", ["string", "int"])
                st.session_state.new_column["type"] = new_column_type
                new_column_example = st.text_input(
                    "Example data", placeholder="Enter comma delimited example values"
                )
                st.session_state.new_column["example"] = new_column_example
                submit = st.form_submit_button("Add Column")
                if submit:
                    with st.spinner("Adding column..."):
                        if new_column:
                            st.session_state.df[new_column] = new_column_type
                            st.session_state.data_type[new_column] = new_column_type
                            st.session_state.example_data[new_column] = new_column_example
                            st.success(f"{new_column} added successfully.")
                            st.rerun()

    if st.session_state.df.columns.tolist():
        # Create a form to take input for column name, datatype from dropdown and example data
        add_column()

    # Button to apply modifications and update the DataFrame
    if st.session_state.df.columns.tolist():
        if st.button("Apply Modifications"):
            try:
                # else do nothing
                if(domain and domain not in st.session_state.domain):
                    st.session_state.domain.append(domain)
                with st.spinner("Applying modifications..."):
                    # Drop the selected columns
                    st.session_state.df.drop(
                        columns=st.session_state.columns_to_remove, inplace=True
                    )
                    # Reset the columns_to_remove list after update
                    st.session_state.columns_to_remove = []
                    st.write("Finalised DataFrame:")
                    st.dataframe(st.session_state.df)
                    # if not os.path.exists("../data"):
                    #     os.mkdir("../data")
                    # st.session_state.df.to_csv(f"""../data/{domain}.csv""", index=False, mode='w')
                    configuration = st.session_state.data_type
                    foreign_key_config = st.session_state.foreign_key
                    final_columns = st.session_state.df.columns.tolist()
                    example_data = st.session_state.example_data
                    if not os.path.exists("../../config"):
                        os.mkdir("../../config")
                    # Save data type and example_data against the columns in a JSON format to a single configuration to a file
                    with open(f"../../config/{domain}_config.json", "w") as f:
                        f.write("{")
                        for column in final_columns:
                            # Split the example data by comma and strip whitespaces
                            examples = (
                                [
                                    example.strip()
                                    for example in example_data[column].split(",")
                                    if example
                                ]
                                if example_data[column]
                                else []
                            )
                            f.write(
                                f'"{column}": {{"data_type": "{configuration[column]}", "example_data": "{examples}", "foreign_key": {foreign_key_config[column]}}}'
                            )
                            if column != final_columns[-1]:
                                f.write(", ")
                        f.write("}")
                    f.close()

                    st.success(f"Data saved as {domain}_config.json")

                    # Add a download button for the JSON file
                    with open(f"../../config/{domain}_config.json", "r") as file:
                        st.download_button(
                            label="Download Configuration",
                            data=file,
                            file_name=f"{domain}_config.json",
                            mime="application/json"
                        )
            except Exception as e:
                st.error(f"An error occurred: {e}")
            except KeyError as ke:
                st.error(f"An error occurred: {ke}")

__all__ = [load_template_generation_component]
