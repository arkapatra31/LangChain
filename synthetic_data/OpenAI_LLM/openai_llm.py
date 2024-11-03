from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import pandas as pd
from langchain.prompts import PromptTemplate

load_dotenv()

# Define the prompt template
template = """
I want {number_of} columns specific to {domain}.
Answer should be precise and should contain only the list of column names and no need to provide numberings.
Also column names should be in lower case and should not have space in between them
"""

# Create a PromptTemplate object
prompt_template = PromptTemplate(template=template, input_variables=["number_of", "domain"])

# Initialize ChatOpenAI
llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini", verbose=True)


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
