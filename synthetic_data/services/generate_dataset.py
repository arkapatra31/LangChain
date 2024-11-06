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
Don't include example data in the generated records but understand and learn from the example data.
Only return the content of the generated records.
Also make sure that the generated records belongs to or are associated to {flavour}.
"""
prompt_template = PromptTemplate(template=template, input_variables=["number", "columns", "data_types", "example_data", "flavour"])


def read_dataframe_and_generate_data(config, number_of_records, flavour):
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
            "example_data": example_data,
            "flavour": flavour
        }
    )

    return response


__all__ = [read_dataframe_and_generate_data]
