from typing import List

from langchain.tools import tool
import os
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document

load_dotenv()

@tool
def extract_md_from_pdf(pdf_path: str) -> List[Document]:
    """
    Extracts markdown content from a PDF file using the `pdf2md` CLI tool.

    Args:
        pdf_path (str): The path to the PDF file to be converted.

    Returns:
        str: The extracted markdown content.
    """
    # set up parser
    parser = LlamaParse(
        api_key= os.getenv("LLAMA_PARSER_API_KEY"),
        result_type="markdown"  # "markdown" and "text" are available
    )

    # use SimpleDirectoryReader to parse our file
    documents = parser.load_data(file_path="SB1100_CD1_.pdf")
    return documents

if __name__ == "__main__":
    # Example usage
    pdf_path = "'SB1100_CD1_.pdf'"  # Replace with your PDF file path
    documents: List[Document] = extract_md_from_pdf(pdf_path)
    for doc in documents:
        with open("SB1100_CD1_.md", "w") as f:
            f.write(doc.text)
        f.close()