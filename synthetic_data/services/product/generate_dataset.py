from langchain_core.prompts import PromptTemplate
from synthetic_data import llm
import pandas as pd


def prompt_with_ref_data():
    # Define the prompt template for generating records based on the example data
    template = """
    I want to generate {number} csv records for the following columns:
    {columns}
    The data type for each column is as follows:
    {data_types}
    The example data for each column is as follows:
    {example_data}
    While generating the records, check if {reference_dataframe} has data and if it has data use that to identify foreign key constraints which can be used in the generated records.
    Always include description for each record which is a unique string and the length of the description should be between 100 and 200.
    Don't include example data in the generated records but understand and learn from the example data.
    Only return the content of the generated records and also don't use comma in values.
    Also make sure that the generated records belongs to or are associated to {flavour}.
    """
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["number", "columns", "data_types", "example_data", "flavour", "reference_dataframe"],
    )
    return prompt_template


def prompt_without_ref_data():
    # Define the prompt template for generating records based on the example data
    template = """
    I want to generate {number} csv records for the following columns:
    {columns}
    The data type for each column is as follows:
    {data_types}
    The example data for each column is as follows:
    {example_data}
    Always include description for each record which is a unique string and the length of the description should be between 100 and 200.
    Don't include example data in the generated records but understand and learn from the example data.
    Only return the content of the generated records and also don't use comma in values.
    Also make sure that the generated records belongs to or are associated to {flavour}.
    """
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["number", "columns", "data_types", "example_data", "flavour"],
    )
    return prompt_template


def read_dataframe_and_generate_data(config, number_of_records, flavour, reference_dataframe):
    # Fetch the prompt template based on the presence of reference data
    prompt_template = prompt_without_ref_data() if (reference_dataframe.empty) else prompt_with_ref_data()

    # Create a chain of operations
    chain = prompt_template | llm

    # Extract the input details from the configuration
    columns = list(config.keys())
    data_types = {col: config[col]["data_type"] for col in columns}
    example_data = {col: config[col]["example_data"] for col in columns}

    # Prepare data for Chain Invocation based on the presence of reference data
    input_data = {
        "number": number_of_records,
        "columns": columns,
        "data_types": data_types,
        "example_data": example_data,
        "flavour": flavour
    }

    # If reference data dataframe is not empty, include it in the input data
    if not reference_dataframe.empty:
        input_data["reference_dataframe"] = reference_dataframe

    # Invoke the chain with the input details
    response = chain.invoke(
        input_data
    )
    return response


__all__ = [read_dataframe_and_generate_data]
