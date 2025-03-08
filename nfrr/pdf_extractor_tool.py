from langchain.tools import tool
import os
import fitz  # PyMuPDF


@tool
def extract_md_from_pdf(pdf_path):
    """
    Convert PDF to Markdown

    Args:
        pdf_path: The file path to the input PDF file.
    """
    if not os.path.exists(pdf_path):
        return f"Error: PDF file not found at path {pdf_path}"

    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        markdown_content = f"# {os.path.basename(pdf_path)}\n\n"

        # Process each page
        for page_num in range(len(doc)):
            page = doc[page_num]

            # Add page number as header
            markdown_content += f"## Page {page_num + 1}\n\n"

            # Extract text
            text = page.get_text()

            # Add the text to markdown content
            markdown_content += text + "\n\n"

        return markdown_content

    except Exception as e:
        return f"Error processing PDF: {str(e)}"


if __name__ == "__main__":
    pdf_path = "RBI.pdf"
    # Now calling the tool using the invoke method
    markdown_content = extract_md_from_pdf.invoke(pdf_path)

    # Save the Markdown content to a file
    with open("output.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)
    print(f"PDF converted to Markdown and saved to output.md")

__all__ = ["extract_md_from_pdf"]