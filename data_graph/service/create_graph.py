from langchain_google_genai import ChatGoogleGenerativeAI
from llms import GeminiLLM
from langchain.prompts import PromptTemplate

def fetchPrompt():
    template = """
    
    LLM Role: Data Analyst 
    
    LLM Job Description:
        - You are a data analyst and you are excellent in analyzing data and finding potential links between data points.
        
    INPUT:
    The {input_data} is a list of CSV files that contains data and are related to each other.
    
    TASK:
        - As your job description, you are required to analyze the data, think carefully, find the nodes and relaitonships between the nodes and prepare a JSON configuration file that contains the nodes and relationships between the nodes.
        
    TASK INSTRUCTIONS:
        - Analyze the data and find the nodes and relationships between the nodes.
        - Prepare a JSON configuration file that contains the nodes and relationships between the nodes.
        
    OUTPUT:
        - Only return the JSON configuration file that contains the nodes and relationships between the nodes
        - DO NOT return any other information.
        
    """

    prompt_template = PromptTemplate(
        template = template,
        input_variables = ['input_data'],
    )

    return prompt_template

def createGraph(input_data):

    # Fetch the prompt template
    prompt_template = fetchPrompt()

    # fetch the llm instance
    llm: ChatGoogleGenerativeAI = GeminiLLM().returnLLMInstance()

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
    createGraph
]