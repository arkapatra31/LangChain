from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import pandas as pd
from langchain.prompts import PromptTemplate
from synthetic_data.OpenAI_LLM.openai_llm import llm

load_dotenv()

# Define the prompt template
template = """
I want {number_of} columns specific to {domain}.
Answer should be precise and should contain only the list of column names and no need to provide numberings.
Also column names should be in lower case and should not have space in between them.
Also make sure that there is one column which can be used as primary key and also other columns which can act
as a foreign key to this table.
"""

# Create a PromptTemplate object
prompt_template = PromptTemplate(template=template, input_variables=["number_of", "domain"])


def get_dataframe_columns(input_details, number_of):
    # Create a chain of operations
    chain = prompt_template | llm

    # Invoke the chain with the input details
    response = chain.invoke(
        {
            "number_of": number_of,
            "domain": input_details
        }
    )

    # Extract columns from the response
    columns = response.content.split('\n')

    return columns
