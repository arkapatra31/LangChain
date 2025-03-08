from pydantic import BaseModel, Field
from typing import Optional
from langchain.output_parsers import PydanticOutputParser

class HeaderExtraction(BaseModel):
    """
    Model to represent the results of header extraction.
    """
    headers: str = Field(description="List of headers extracted from the PDF document")
    subheaders: Optional[str] = Field(
        default=None,
        description="List of subheaders extracted from the PDF document"
    )
    content: str = Field(description="The extracted content from the PDF document")

class MarkdownHeaderExtraction(BaseModel):
    """
    Model to represent the results of PDF extraction.
    """
    title: str = Field(description="The title of the PDF document")
    content: list[HeaderExtraction] = Field(
        description="List of headers and their associated content extracted from the PDF document"
    )

class PDFExtractionOutputparser(PydanticOutputParser):
    """
    Parser for PDF extraction results.
    """

    def __init__(self):
        super().__init__(pydantic_object=MarkdownHeaderExtraction)

    @property
    def _type(self) -> str:
        return "pdf_extraction_results"

    def get_format_instructions(self) -> str:
        """Return the formatted output instructions."""
        return """Return the PDF extraction results in the following format:
                {
                    "title": "PDF Title",
                    "content": [
                        {
                            "headers": "Header 1",
                            "subheaders": "Subheader 1",
                            "content": "Content associated with Header 1"
                        },
                        {
                            "headers": "Header 2",
                            "subheaders": "Subheader 2",
                            "content": "Content associated with Header 2"
                        }
                    ]
                }
        """


# Create a single instance of the output parser
pdf_extraction_output_parser = PDFExtractionOutputparser()

if __name__ == "__main__":
    print(pdf_extraction_output_parser.get_format_instructions())

__all__ = [pdf_extraction_output_parser]
