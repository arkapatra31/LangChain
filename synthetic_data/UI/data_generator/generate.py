import streamlit as st
import pandas as pd
import json
import os
from synthetic_data import (
    generate_address_for_EU,
    generate_address_for_US,
    read_dataframe_and_generate_data,
)
from synthetic_data.customer_generation.main import generate_customers
from synthetic_data.order_generation.main import generate_order_data
from synthetic_data.order_line_item_generation.main import (
    generate_order_line_items_data,
)


# Set page configuration
st.set_page_config(page_title="Data Generator", page_icon="📊", layout="centered")

# Load custom CSS for dark theme and glowing effects
with open("../assets/data_generate_styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Data Generator")

domain = st.selectbox(
    "Select domain from the following",
    ["Product", "Customer", "Order", "OrderDetails"],
    key="domain",
)

if domain == "Product":
    number_of_records = st.number_input(
        "Enter the number of records to generate", min_value=1, max_value=100, step=1
    )
    flavor = st.text_input(
        "Enter the domain flavor", value="", placeholder="Enter the domain flavor"
    )
    uploaded_file = st.file_uploader("Upload JSON Configuration File", type="json")

    if uploaded_file is not None:
        file_name = uploaded_file.name.split("_")[0]
        config = json.loads(uploaded_file.getvalue().decode("utf-8"))

        if st.button("Generate Product Data"):
            response = read_dataframe_and_generate_data(
                config, number_of_records, flavor
            )
            content = response.content
            data = [row.split(",") for row in content.split("\n") if row]
            columns = list(config.keys())
            sanitized_data = [idv_data for idv_data in data if len(idv_data) == len(columns)]
            df = pd.DataFrame(sanitized_data, columns=columns)
            df.dropna(inplace=True)
            df.drop(df.index[[0]], inplace=True)
            df.reset_index(drop=True, inplace=True)

            if not os.path.exists("../../data/products"):
                os.makedirs("../../data/products")
            csv_file_path = f"../../data/products/{file_name}_data.csv"
            df.to_csv(csv_file_path, index=False)
            st.success(f"Data saved as {csv_file_path}")
            st.dataframe(df)

elif domain == "Customer":
    customer_address = st.selectbox(
        "Select address type", ["US", "EU"], key="address_type"
    )
    number_of_records = st.number_input(
        "Enter the number of records to generate", min_value=1, max_value=1000, step=1
    )

    if st.button("Generate Customer Data"):
        if customer_address == "US":
            generate_address_for_US()
        else:
            generate_address_for_EU()

        customer_df = generate_customers(number_of_records)
        if customer_df is not None:
            st.success("Customer data generated successfully")
            st.dataframe(customer_df)

elif domain == "Order":
    number_of_records = st.number_input(
        "Enter the number of records to generate", min_value=1, max_value=1000, step=1
    )
    external_csv_usage = st.checkbox(
        "Use any dependent CSV for records creation ?", value=False
    )

    if external_csv_usage:
        uploaded_file = st.file_uploader(
            "Upload the dependent CSV files", type="csv", accept_multiple_files=True
        )

        if uploaded_file is not None:
            df_list = [pd.read_csv(file) for file in uploaded_file]

        if st.button("Generate Order Data"):
            order_df = generate_order_data(number_of_records, df_list)
            if order_df is not None:
                st.success("Order data generated successfully")
                st.dataframe(order_df)

elif domain == "OrderDetails":
    number_of_records = st.number_input(
        "Enter the number of records to generate", min_value=1, max_value=1000, step=1
    )
    external_csv_usage = st.checkbox(
        "Use any dependent CSV for records creation ?", value=False
    )
    record_mismatch = False

    if external_csv_usage:
        uploaded_file = st.file_uploader(
            "Upload the dependent CSV files", type="csv", accept_multiple_files=True
        )

        if uploaded_file is not None:
            df_list = []
            for file in uploaded_file:
                file_name = file.name.split("_")[0]
                if "orders" in file_name:
                    order_df = pd.read_csv(file)
                    if len(order_df) != number_of_records:
                        record_mismatch = True
                        st.error(
                            "Number of records in order file should be equal to the number of records to generate"
                        )
                        break
                    else:
                        df_list.append(order_df)
                else:
                    df = pd.read_csv(file)
                    df_list.append(df)

        if not record_mismatch:
            if st.button("Generate Order Line Items"):
                order_line_df = generate_order_line_items_data(
                    number_of_records, df_list
                )
                if order_line_df is not None:
                    st.success("Order Line Items data generated successfully")
                    st.dataframe(order_line_df)