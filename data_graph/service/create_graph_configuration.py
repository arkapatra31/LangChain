from langchain_google_genai import ChatGoogleGenerativeAI
from llms import gemini_llm
from langchain.prompts import PromptTemplate

def fetchPromptForJSONConfiguration():
    template = """
        DEFINE LLM ROLE:
        - You are a Data Analyst and you are excellent in analyzing data and mapping them with 0 data loss

        INPUT:
        Here is your input data:
        {input_data}

        TASK DESCRIPTION:
        You need to analyse the records and then return only the JSON content in JSON format. The JSON format details are as follows:
        1. nodes: Dictionary of nodes with the following details:
            - id: str = Unique identifier of the node
            - label: str =  Label of the node
            - properties: Optional[dict] = Properties of the node
        2. relationships: List of relationships with the following details:
            - sourceId: str = Unique identifier of the source node
            - targetId: str = Unique identifier of the target node
            - label: str = Label of the relationship
            - properties: Optional[dict] = Properties of the relationship containing a foreign key and the value

        IMPORTANT:
        Make sure do not return any other information or metadata
    """

    # template = """
    #         DEFINE LLM ROLE:
    #         - You are a Data Analyst and you are excellent in analyzing data and mapping them with 0 data loss
    #
    #         INPUT:
    #         Here is your input data:
    #         {input_data}
    #
    #         TASK DESCRIPTION:
    #         You need to analyse the records and then return only the JSON content in JSON format. The JSON format details are as follows:
    #         1. nodes: Dictionary of nodes with all the details of the rows in the input data
    #
    #         2. relationships: List of relationships with all the links between the nodes in the input data
    #
    #         IMPORTANT:
    #         Make sure do not return any other information or metadata
    #     """

    prompt_template = PromptTemplate(
        template=template,
        input_variables=['input_data']
        # partial_variables={
        #     "format": output_parser.get_format_instructions()
        # }
    )

    return prompt_template

def createGraphConfiguration(input_data) :
    # Fetch the prompt template
    prompt_template = fetchPromptForJSONConfiguration()

    # Fetch the llm instance
    llm: ChatGoogleGenerativeAI = gemini_llm

    # LCEL for creating the chain
    chain = prompt_template | llm #| output_parser

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