from typing import List
from langchain.tools import tool
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document

load_dotenv()

@tool
def extract_md(md_path: str) -> List[Document]:
    """
    Name:     extract_md
    Purpose:  Extracts markdown content from a PDF file using the UnstructuredMarkdownLoader.
    Args:
        md_path (str): The path to the PDF file to be converted.
    Returns:
        List[Document]: A list of Document objects containing the extracted markdown content.
    """
    try:
        # Try using UnstructuredMarkdownLoader first (better Markdown parsing)
        loader = UnstructuredMarkdownLoader(md_path)
        documents = loader.load()
        return documents
    except Exception as e:
        print(f"Warning: UnstructuredMarkdownLoader failed, falling back to TextLoader: {e}")
        raise e

__all__ = [extract_md]

if __name__ == "__main__":
    # Example usage
    documents = extract_md("./Generated_MD/output.md")
    print(documents)