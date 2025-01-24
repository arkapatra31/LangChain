from langchain_google_genai import ChatGoogleGenerativeAI
from llms import gemini_llm
from langchain.prompts import PromptTemplate

def fetchPromptForJSONConfiguration():
    template = """
    
    LLM Role: Data Analyst 
    
    LLM Job Description:
        - You are a data analyst and you are excellent in analyzing data and finding potential links between data points.
        
    INPUT:
    The {input_data} is a list of CSV files that contains data and are related to each other.
    
    TASK:
        - Analyze the data, find the nodes and relationships between the nodes
        
    TASK INSTRUCTIONS:
        - Analyze the data and find the nodes and relationships between the nodes.
        - Prepare a JSON configuration file that contains the nodes and relationships between the nodes which should include the following:
            - Nodes: The nodes should contain the following information:
                - id: The unique identifier of the node
                - label: The label of the node
                - properties: The properties of the node
            - Relationships: The relationships between the nodes should contain the following information:
                - id: The unique identifier of the relationship
                - source: The source node of the relationship
                - target: The target node of the relationship
                - label: The label of the relationship
                - properties: The properties of the relationship or  the key used to connect the nodes. 
        
    OUTPUT:
        - Only return the JSON configuration file that contains the nodes and relationships between the nodes
        - DO NOT return any other information.
        
    """

    prompt_template = PromptTemplate(
        template = template,
        input_variables = ['input_data'],
    )

    return prompt_template

def createGraphConfiguration(input_data):

    # Fetch the prompt template
    prompt_template = fetchPromptForJSONConfiguration()

    # fetch the llm instance
    llm: ChatGoogleGenerativeAI = gemini_llm

    # LCEL for creating the chain
    chain = prompt_template | llm

    # Execute the chain
    response = chain.invoke(
        {
            "input_data": input_data
        }
    )

    return response.content

__all__ = [
    createGraphConfiguration
]