import streamlit as st
import pandas as pd
import json
import os
from synthetic_data import generate_address_for_EU, generate_address_for_US, read_dataframe_and_generate_data
from synthetic_data.customer_generation.main import generate_customers
from synthetic_data.order_generation.main import generate_order_data

st.title("Data Generator")

domain = st.selectbox("Select domain from the following", ["Product", "Customer", "Order"], key="domain")

if domain == "Product":
    # Take the number of records to generate
    number_of_records = st.number_input("Enter the number of records to generate", min_value=1, max_value=100, step=1)

    # Take input for the domain flavor
    flavor = st.text_input("Enter the domain flavor", value="", placeholder="Enter the domain flavor")

    # File uploader to accept JSON configuration file
    uploaded_file = st.file_uploader("Upload JSON Configuration File", type="json")

    if uploaded_file is not None:

        # Fetch name of the uploaded config file
        file_name = uploaded_file.name.split("_")[0]

        # Parse the JSON file
        config = json.loads(uploaded_file.getvalue().decode("utf-8"))

        if st.button("Generate Product Data"):
            # Generate DataFrame based on the configuration
            response = read_dataframe_and_generate_data(config, number_of_records, flavor)

            # Extract the content from the response
            content = response.content
            # st.success(content)

            # Convert the content into a DataFrame
            data = [row.split(",") for row in content.split("\n") if row]
            # Convert config keys into list
            columns = list(config.keys())

            # Sanitize the data to make sure it retains only the values that are equal to the number of columns
            sanitized_data = []
            for idv_data in data:
                if len(idv_data) != len(columns):
                    # delete the data
                    data.remove(idv_data)

            df = pd.DataFrame(data, columns=columns)
            # Drop the records with missing values and the column names
            df.dropna(inplace=True)

            # Drop the first row which is the column names
            df.drop(df.index[[0]], inplace=True)

            # Reset the index
            df.reset_index(drop=True, inplace=True)

            # Save the DataFrame to a CSV file
            # Check if the generated_data directory exists
            if not os.path.exists("../../data/products"):
                os.makedirs("../../data/products")
            csv_file_path = f"../../data/products/{file_name}_data.csv"
            df.to_csv(csv_file_path, index=False)
            st.success(f"Data saved as {csv_file_path}")
            # Display the DataFrame
            st.dataframe(df)


elif domain == "Customer":
    customer_address = st.selectbox("Select address type", ["US", "EU"], key="address_type")

    number_of_records = st.number_input("Enter the number of records to generate", min_value=1, max_value=1000, step=1)

    if st.button("Generate Customer Data"):
        if customer_address == "US":
            generate_address_for_US()
        else:
            generate_address_for_EU()

        customer_df = generate_customers(number_of_records)
        if customer_df is not None:
            st.success("Customer data generated successfully")
            st.dataframe(customer_df)

elif (domain == "Order"):
    # Take the number of records to generate
    number_of_records = st.number_input("Enter the number of records to generate", min_value=1, max_value=1000, step=1)

    # Take input to check if records needs some external CSV file or not
    external_csv_usage = st.checkbox("Use any dependent CSV for records creation ?", value=False)

    if external_csv_usage:
        # File uploader to accept JSON configuration file
        uploaded_file = st.file_uploader("Upload the dependent CSV files", type="csv", accept_multiple_files=True)

        # Check if file is uploaded or not
        if uploaded_file is not None:
            df_list = []
            # Read the uploaded file
            for file in uploaded_file:
                # Parse the CSV content and convert it to DataFrame
                df = pd.read_csv(file)
                df_list.append(df)

        if st.button("Generate Order Data"):
            order_df = generate_order_data(number_of_records, df_list)
            if order_df is not None:
                st.success("Order data generated successfully")
                st.dataframe(order_df)
