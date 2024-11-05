import os
import json
import streamlit as st
import pandas as pd
from synthetic_data import read_dataframe_and_generate_data

# Streamlit UI
st.title("Generate DataFrame from Configuration")

# File uploader to accept JSON configuration file
uploaded_file = st.file_uploader("Upload JSON Configuration File", type="json")

# Take the number of records to generate
number_of_records = st.number_input("Enter the number of records to generate", min_value=1, max_value=100, step=1)

if uploaded_file is not None:

    # Fetch name of the uploaded config file
    file_name = uploaded_file.name.split("_")[0]

    # Parse the JSON file
    config = json.loads(uploaded_file.getvalue().decode("utf-8"))

    # Generate DataFrame based on the configuration
    response = read_dataframe_and_generate_data(config, number_of_records)

    # Extract the content from the response
    content = response.content
    # st.success(content)

    # Convert the content into a DataFrame
    data = [row.split(",") for row in content.split("\n") if row]
    columns = list(config.keys())
    df = pd.DataFrame(data, columns=columns)

    # Drop the records with missing values and the column names
    df.dropna(inplace=True)

    # Reset the index
    df.reset_index(drop=True, inplace=True)

    # Drop the first row which is the column names
    df.drop(df.index[[0]], inplace=True)

    # Save the DataFrame to a CSV file
    # Check if the generated_data directory exists
    if not os.path.exists("../generated_data"):
        os.mkdir("../generated_data")
    csv_file_path = f"../generated_data/{file_name}_data.csv"
    df.to_csv(csv_file_path, index=False)
    st.success(f"Data saved to {csv_file_path}")
    st.dataframe(df)
