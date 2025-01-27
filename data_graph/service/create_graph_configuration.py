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
        You need to analyse the records and then return only the JSON content in JSON format.
        
        OUTPUT FORMAT:
        ```json
        {{
            "nodes": [
                {{
                    "id": "node id",
                    "label": "node label",
                    "type": "Node",
                    "properties": {{
                        "property1": "property1 value",
                        "property2": "property2 value"
                    }}
                }}
            ],
            "relationships": [
                {{
                    "source": "source node id",
                    "target": "target node id",
                    "type": "Relationship Type",
                    "properties": {{
                        'source_id': 'source node id',
                        'target_id': 'target node id'
                }}
            ]
        }}
        ```
        
        THOUGHT PROCESS to follow:
        While transforming the data to JSON, follow the below steps:
        1. *** Iterate through all the rows during creating nodes ***:
                - From input data, iterate over every row in the input_data and create nodes
                - Do not stop after processing first rows. Continue processing until all rows are included
        2. *** Extract All related Entities during creating relationships ***:
                - For every related entity, check all rows from the input_data to ensure no entity is missed out.
                - Do not stop after extracting the first few related entities. Continue processing rows until all matches are included.
                
        IMPORTANT INSTRUCTIONS TO FOLLOW:
                - Verify that every records from the input data are included in the nodes of the JSON, if not include them in the nodes
                - Ensure no rows are missed out from output, if missed out, include them in the nodes
                - Ensure the relationships are properly mapped with the nodes, if not validate and correct them
                - Ensure all the above being considered, return the JSON output with zero data loss.
        
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