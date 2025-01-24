from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from llms import gemini_llm


def fetch_prompt_template():
    template = """
    
    LLM Role: Data Analyst  & Neo4j Developer
    
    LLM Job Description:
        - You are a data analyst and you are excellent in analyzing data and finding potential links between data points.
        - You are also a Neo4j Developer and you are excellent in writing Cypher queries that will load the data into Neo4j
        
    INPUT:
        You will have two input variables:
        - The {csv_list} is a list of CSV files that contains data and are related to each other.
        - A {json_config} which is a JSON configuration where the nodes and relationships between the nodes are defined
        
    TASK:
        - Always open the csv file in encoding='utf-8'
        - Analyze both the csv and the json_config thoroughly to create a Cypher query that will load the data into Neo4j
        - While writing the Cypher query, make sure that the nodes and relationships between the nodes are properly defined
        - While writing the Cypher query, do not use LOAD CSV instead use the raw values from the DataFrames
        - While using the raw values from the DataFrames, make sure the entire data is loaded into Neo4j
        - While writing the Cypher query, always refer documentation for the correct syntax
        
    OUTPUT:
        - Only return the raw Cypher query that will load the data into Neo4j
        
    """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=['csv_list', 'json_config']
    )

    return prompt_template


def create_cypher_query(csv_list, json_config):
    # Fetch the prompt template
    prompt_template = fetch_prompt_template()

    # fetch the llm instance
    llm: ChatGoogleGenerativeAI = gemini_llm

    # LCEL for creating the chain
    chain = prompt_template | llm

    # Execute the chain
    response = chain.invoke(
        {
            "csv_list": csv_list,
            "json_config": json_config
        }
    )
    return response.content


__all__ = [
    create_cypher_query
]
