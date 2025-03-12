from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from nfrr.anthropic_llm import anthropic_llm
from nfrr.pdf_extractor_tool import extract_md_from_pdf
from nfrr.md_tool import extract_md
from nfrr.output_parser import pdf_extraction_output_parser
import json


def invoke_pdf_agent(md_path: str):
    """
    This function invokes the PDF agent to extract headers and their associated content from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file to be processed.

    Returns:
        str: The JSON formatted output containing headers and their associated content.
    """
    # Define the system and human prompts
    system_prompt = SystemMessagePromptTemplate.from_template(
        template="""
                    You are an AI assistant with the capability to read markdown content and return the output in JSON format of headers, subheaders and their associated content.
                    You will be calling a tool named `extract_md` with the markdown file path coming from input to read the markdown content
                    Once the tool returns the markdown content, you will analyze it and extract all headers and their associated content.
                    You should maintain the hierarchical structure of the document, correctly identify main headers and subheaders, associate the relevant content with each header, and format the output in clean, well-structured JSON.
                    You should include the headers / subheaders and the associated content if missed by the tool.
                    You are supposed to return the output in the following format: {format} and strictly follow the format.
                    STRICTLY, DO NOT include any metadata or any other additional information in the output.
        """
    )

    # Define the human message prompt
    human_message = HumanMessagePromptTemplate.from_template(
        template="""
                        Please analyze the Markdown content from the file path :  {md_path}
                        Extract all headers and their associated content, and return them in a JSON format.
                        This is a Banking and Finance document, so please ensure that the each and every information is account for including the headers and subheaders and the content associated with them.
                        Write down your thoughts and reasoning in the {agent_scratchpad}.
        """
    )

    prompt_template = ChatPromptTemplate.from_messages(
        [system_prompt, human_message]
    )

    llm = anthropic_llm()

    tools = [extract_md]

    agent = create_tool_calling_agent(
        llm, tools, prompt_template
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )

    response = agent_executor.invoke(
        {
            "md_path": md_path,
            "format": pdf_extraction_output_parser.get_format_instructions(),
            "agent_scratchpad": []
        }
    )
    output = response.get("output")[0]['text']

    # Convert output to JSON
    return output


if __name__ == "__main__":
    response = invoke_pdf_agent("./Generated_MD/SB1100_CD1_.md")
    print(response)
