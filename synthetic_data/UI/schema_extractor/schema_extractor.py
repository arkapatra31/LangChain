import os, json
import pandas as pd
from synthetic_data import prepare_template_schema


def extractSchema(st):
    # Streamlit UI
    st.title("Template Extractor")
    st.write("Extract schema from your data and customise it as per your requirements.")

    uploaded_file = st.file_uploader("Choose a file", type="csv", key="file_uploader", accept_multiple_files=False)
    extract_data = st.radio("Use Data as reference values ?", ["Yes", "No"])

    if uploaded_file is not None:
        st.session_state.df = pd.read_csv(uploaded_file)

    if st.button("Extract Schema"):
        with st.spinner("Extracting Schema..."):
            data_template = prepare_template_schema(st.session_state.df, extract_data)
            st.session_state.schema = data_template
            st.success("Schema extracted successfully.")

    if  st.session_state.schema:
        # Display the schema extracted from the uploaded file
        column_name, data_type, remove_label, example_label, foreign_key_label = st.columns([1.8, 1.5, 1.8, 2.5, 2])
        column_name.write("Column Name")
        data_type.write("Data Type")
        remove_label.write("Remove ?")
        example_label.write("Example Data")
        foreign_key_label.write("Foreign Key ?")

        col1, col2, col3, col4, col5 = st.columns([1.8, 1.5, 1.8, 2.5, 2])
        for column in st.session_state.schema.keys():

            col1.write(column)

            col2.write(st.session_state.schema.get(column).get("data_type"))

            remove = col3.checkbox(
                "Remove",
                key=f"remove_{column}",
                value=column in st.session_state.columns_to_remove
            )
            if remove:
                if column not in st.session_state.columns_to_remove:
                    st.session_state.columns_to_remove.append(column)
            else:
                if column in st.session_state.columns_to_remove:
                    st.session_state.columns_to_remove.remove(column)

            col4.write("Dataset Referred" if  extract_data == "Yes" else [])

            is_foreign_key = col5.checkbox("Foreign Key", key=f"foreign_key_{column}")
            if is_foreign_key:
                st.session_state.foreign_key[column] = 1
            else:
                st.session_state.foreign_key[column] = 0


    if st.session_state.schema:
        if st.button("Generate Final Schema"):
            # Remove the columns that are selected to be removed
            if len(st.session_state.columns_to_remove) > 0:
                for column in st.session_state.columns_to_remove:
                    st.session_state.schema.pop(column)
                st.session_state.columns_to_remove = []

            # Assign foreign key to the columns in the schema
            for column in st.session_state.schema.keys():
                st.session_state.schema.get(column)["foreign_key"] = st.session_state.foreign_key.get(column)
            st.session_state.foreign_key = {}

            st.write("Final Schema")
            # Write a JSON file with the final schema with a download button
            st.write(st.session_state.schema)
            json_file = json.dumps(st.session_state.schema, indent=4)
            st.download_button(
                label="Download Schema",
                data=json_file,
                file_name="schema.json",
                mime="application/json",
            )


__all__ = [
    extractSchema
]
