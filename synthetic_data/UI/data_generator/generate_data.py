import streamlit as st
import pandas as pd
import json
import os
import random

from pandas import DataFrame
from synthetic_data import (
    generate_address_for_EU,
    generate_address_for_US,
    read_dataframe_and_generate_data,
    read_dataframe_and_generate_data_with_faker
)
from synthetic_data.customer_generation.main import generate_customers
from synthetic_data.order_generation.main import generate_order_data
from synthetic_data.order_line_item_generation.main import (
    generate_order_line_items_data,
)


def load_data_generation_component(st):
    st.title("Data Generator")
    domain_to_be_populated = []

    # Capture the domains for which the user is generating the template
    if st.session_state.domain is not None and st.session_state.domain != []:
        domain_to_be_populated.extend(st.session_state.domain)
    else:
        domain_to_be_populated.extend(["Banks", "Customers", "Medical Insurance", "Customer", "Order", "OrderDetails"])

    # Create a select box for domain along with the unique key.
    col1, col2 = st.columns([3, 1])
    with col1:
        domain = st.selectbox("Select domain of data you are looking for", domain_to_be_populated)
    with col2:
        st.info("Click on the refresh button to refresh the domains")
        refresh_button = st.button("🔃")

        if refresh_button:
            st.rerun()

    # domain = st.selectbox("Select domain of data you are looking for", domain_to_be_populated)

    # st.session_state.domain = domain

    if domain == "Customer":
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

    elif domain:

        # Accept the number of records to generate
        number_of_records = st.number_input(
            "Enter the number of records to generate", min_value=1, max_value=100, step=1
        )

        # Accept the domain flavor
        flavor = st.text_input(
            "Enter the domain flavor", value="", placeholder="Enter the domain flavor"
        )

        # Accept the JSON configuration file
        uploaded_file = st.file_uploader("Upload JSON Configuration File", type="json")

        if uploaded_file is not None:
            file_name = uploaded_file.name.split("_")[0]
            if file_name != domain:
                return st.error(f"Template configuration file name should start with {domain}")

            # Checkbox for uploading dependent CSV files. Also while clicking on the checkbox it will display a notice message
            external_csv_usage = st.checkbox(
                "Use any dependent CSV for records creation ?", value=False, key="external_csv_usage",
                help="Only upload the dependent CSV files if required"
            )

            # Initialize the reference DataFrame
            reference_df: DataFrame = pd.DataFrame()
            # If the checkbox is checked, then upload the dependent CSV files
            if external_csv_usage:
                related_csv = st.file_uploader(
                    "Upload the dependent CSV files", type="csv", accept_multiple_files=True, key="related_csv"
                )

                # Load the CSV files and merge into a single DataFrame for further processing
                if related_csv is not None:
                    df_list = [pd.read_csv(file) for file in related_csv]
                    if df_list and len(df_list) > 0:
                        reference_df = pd.concat(df_list, axis=1)
                else:
                    reference_df = None

            # Load the JSON configuration file
            try:
                config = json.loads(uploaded_file.getvalue().decode("utf-8"))
            except json.JSONDecodeError:
                st.error("The uploaded file is not a valid JSON file. Please upload a valid JSON configuration file.")
            except Exception as e:
                st.error(f"An error occurred while processing the file: {e}")

            # Generate the data based on the configuration
            if st.button("Generate Product Data"):
                df = read_dataframe_and_generate_data(
                    domain, config, number_of_records, flavor, reference_df
                )

                if not os.path.exists("../../data/products"):
                    os.makedirs("../../data/products")
                csv_file_path = f"../../data/products/{file_name}_data.csv"
                df.to_csv(csv_file_path, index=False)
                st.success(f"Data saved as {csv_file_path}")
                # Display the generated data
                csv = df.to_csv(index=False).encode('utf-8')
                st.dataframe(df)
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name=f"{domain}_data.csv",
                    mime='text/csv',
                )


def remove_circular_references(obj, seen=None):
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return None
    seen.add(obj_id)
    if isinstance(obj, dict):
        return {k: remove_circular_references(v, seen) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [remove_circular_references(i, seen) for i in obj]
    elif isinstance(obj, tuple):
        return tuple(remove_circular_references(i, seen) for i in obj)
    elif isinstance(obj, set):
        return {remove_circular_references(i, seen) for i in obj}
    return obj

def load_data_generation_component_with_faker(st):
    st.title("Data Generator")
    domain_to_be_populated = []

    # Capture the domains for which the user is generating the template
    if st.session_state.domain is not None and st.session_state.domain != []:
        domain_to_be_populated.extend(st.session_state.domain)
    else:
        domain_to_be_populated.extend([ "Customer", "Order", "OrderDetails"])

    # Create a select box for domain along with the unique key.
    col1, col2 = st.columns([3, 1])
    with col1:
        domain = st.selectbox("Select domain of data you are looking for", domain_to_be_populated)
    with col2:
        st.info("Click on the refresh button to refresh the domains")
        refresh_button = st.button("🔃")

        if refresh_button:
            st.rerun()

    if domain:

        # Accept the number of records to generate
        number_of_records = st.number_input(
            "Enter the number of records to generate", min_value=1, max_value=1000, step=10
        )

        # Accept the JSON configuration file
        uploaded_file = st.file_uploader("Upload JSON Configuration File", type="json")

        if uploaded_file is not None:
            file_name = uploaded_file.name.split("_")[0]
            if file_name != domain:
                return st.error(f"Template configuration file name should start with {domain}")

            # Checkbox for uploading dependent CSV files. Also while clicking on the checkbox it will display a notice message
            external_csv_usage = st.checkbox(
                "Use any dependent CSV for records creation ?", value=False, key="external_csv_usage",
                help="Only upload the dependent CSV files if required"
            )

            # Initialize the reference DataFrame
            reference_df: DataFrame = pd.DataFrame()
            # If the checkbox is checked, then upload the dependent CSV files
            if external_csv_usage:
                related_csv = st.file_uploader(
                    "Upload the dependent CSV files", type="csv", accept_multiple_files=True, key="related_csv"
                )

                # Load the CSV files and merge into a single DataFrame for further processing
                if related_csv is not None:
                    df_list = [pd.read_csv(file) for file in related_csv]
                    if df_list and len(df_list) > 0:
                        reference_df = pd.concat(df_list, axis=1)
                else:
                    reference_df = None

            # Load the JSON configuration file
            try:
                config = json.loads(uploaded_file.getvalue().decode("utf-8"))
            except json.JSONDecodeError:
                st.error("The uploaded file is not a valid JSON file. Please upload a valid JSON configuration file.")
            except Exception as e:
                st.error(f"An error occurred while processing the file: {e}")

            # Generate the data based on the configuration
            if st.button("Generate Product Data"):
                df = read_dataframe_and_generate_data_with_faker(domain, config, number_of_records, reference_df)
                st.dataframe(df)

                # if not os.path.exists("../../data/products"):
                #     os.makedirs("../../data/products")
                # csv_file_path = f"../../data/products/{file_name}_data.csv"
                # df.to_csv(csv_file_path, index=False)
                # st.success(f"Data saved as {csv_file_path}")
                # # Display the generated data
                # csv = df.to_csv(index=False).encode('utf-8')
                # st.dataframe(df)
                # st.download_button(
                #     label="Download data as CSV",
                #     data=csv,
                #     file_name=f"{domain}_data.csv",
                #     mime='text/csv',
                # )


__all__ = [load_data_generation_component, load_data_generation_component_with_faker]
