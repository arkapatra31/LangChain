from langchain_core.prompts import PromptTemplate
from synthetic_data import llm

# Define the prompt template for generating records based on the example data
template = """
I want to generate {number} csv records for the following columns:
{columns}
The data type for each column is as follows:
{data_types}
The example data for each column is as follows:
{example_data}
Try to generate the records based on the example data provided but do not copy the example data directly.
Remember reference data should be used only for reference and not for generating the records.
Only return the content of the generated records.
"""
prompt_template = PromptTemplate(template=template, input_variables=["number", "columns", "data_types", "example_data"])


def read_dataframe_and_generate_data(config, number_of_records):
    # Create a chain of operations
    chain = prompt_template | llm

    # Extract the input details from the configuration
    columns = list(config.keys())
    data_types = {col: config[col]["data_type"] for col in columns}
    example_data = {col: config[col]["example_data"] for col in columns}

    # Invoke the chain with the input details
    response = chain.invoke(
        {
            "number": number_of_records,
            "columns": columns,
            "data_types": data_types,
            "example_data": example_data
        }
    )

    return response


__all__ = [read_dataframe_and_generate_data]
