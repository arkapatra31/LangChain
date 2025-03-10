import os
import fitz  # PyMuPDF
import re
from typing import List, Dict, Set, Tuple
import statistics


class PDFElement:
    def __init__(self, text: str, font_size: float, font_flags: int, bbox: tuple):
        self.text = text
        self.font_size = font_size
        self.font_flags = font_flags
        self.bbox = bbox
        self.is_bold = bool(font_flags & 2 ** 4)  # Check if text is bold
        self.left_margin = bbox[0]
        self.top_margin = bbox[1]


def extract_md_from_pdf(pdf_path: str) -> str:
    """
    Generic PDF to Markdown converter that preserves document structure and formatting.

    Args:
        pdf_path: Path to the PDF file
    Returns:
        Markdown formatted string
    """

    def analyze_document_structure(doc) -> Tuple[float, float, float, Set[float]]:
        """Analyze document to determine font sizes for different heading levels."""
        font_sizes: List[float] = []
        margins: List[float] = []

        for page in doc:
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" not in block:
                    continue
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["text"].strip():
                            font_sizes.append(span["size"])
                            margins.append(span["bbox"][0])

        if not font_sizes:
            return 16, 14, 12, set()

        # Sort font sizes in descending order
        font_sizes.sort(reverse=True)
        common_margins = set(round(m, 1) for m in margins)

        # Calculate thresholds based on distribution
        h1_size = statistics.mean(font_sizes[:max(3, len(font_sizes) // 20)])
        h2_size = statistics.mean(font_sizes[len(font_sizes) // 20:len(font_sizes) // 10])
        h3_size = statistics.mean(font_sizes[len(font_sizes) // 10:len(font_sizes) // 5])

        return h1_size, h2_size, h3_size, common_margins

    def is_list_item(text: str, left_margin: float, common_margins: Set[float]) -> bool:
        """Detect if text is a list item."""
        list_patterns = [
            r'^\s*[\-\•\*]\s+',  # Bullet points
            r'^\s*\d+[\.\)]\s+',  # Numbered lists
            r'^\s*[a-z][\.\)]\s+',  # Alphabetical lists
            r'^\s*[A-Z][\.\)]\s+'  # Capital letter lists
        ]

        is_indented = any(abs(left_margin - m) < 1 for m in common_margins if m > min(common_margins))
        has_list_marker = any(re.match(pattern, text) for pattern in list_patterns)

        return has_list_marker or (is_indented and len(text.strip()) < 100)

    def process_text_block(text: str, font_size: float, is_bold: bool,
                           h1_size: float, h2_size: float, h3_size: float) -> str:
        """Process text block and return appropriate markdown formatting."""
        text = text.strip()

        if not text:
            return ""

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)

        # Determine heading level
        if font_size >= h1_size:
            return f"## {text}\n\n"
        elif font_size >= h2_size and is_bold:
            return f"### {text}\n\n"
        elif font_size >= h3_size and is_bold:
            return f"#### {text}\n\n"

        return f"{text}\n\n"

    if not os.path.exists(pdf_path):
        return f"Error: PDF file not found at path {pdf_path}"

    try:
        doc = fitz.open(pdf_path)
        markdown_content: List[str] = []

        # Analyze document structure
        h1_size, h2_size, h3_size, common_margins = analyze_document_structure(doc)

        # Add document title
        title = os.path.splitext(os.path.basename(pdf_path))[0]
        markdown_content.append(f"# {title}\n\n")

        current_list_items: List[str] = []
        in_list = False

        for page in doc:
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" not in block:
                    continue

                block_text = ""
                block_properties = PDFElement("", 0, 0, (float('inf'), 0, 0, 0))

                # Process all spans in the block
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if not text:
                            continue

                        block_text += text + " "
                        block_properties = PDFElement(
                            text=block_text,
                            font_size=max(block_properties.font_size, span["size"]),
                            font_flags=span["flags"],
                            bbox=span["bbox"]
                        )

                if not block_text.strip():
                    continue

                # Clean up block text
                block_text = block_text.strip()

                # Check if this is a list item
                if is_list_item(block_text, block_properties.left_margin, common_margins):
                    if not in_list:
                        if current_list_items:
                            markdown_content.append("\n".join(current_list_items) + "\n\n")
                            current_list_items = []
                        in_list = True
                    current_list_items.append(block_text)
                else:
                    # Handle non-list content
                    if in_list and current_list_items:
                        markdown_content.append("\n".join(current_list_items) + "\n\n")
                        current_list_items = []
                        in_list = False

                    formatted_text = process_text_block(
                        block_text,
                        block_properties.font_size,
                        block_properties.is_bold,
                        h1_size, h2_size, h3_size
                    )
                    markdown_content.append(formatted_text)

        # Add any remaining list items
        if current_list_items:
            markdown_content.append("\n".join(current_list_items) + "\n\n")

        # Close the document
        doc.close()

        # Join all content and clean up
        final_content = "".join(markdown_content)

        # Clean up excessive newlines and spaces
        final_content = re.sub(r'\n{3,}', '\n\n', final_content)
        final_content = re.sub(r' {2,}', ' ', final_content)

        return final_content

    except Exception as e:
        return f"Error processing PDF: {str(e)}"


if __name__ == "__main__":
    pdf_path = "test.pdf"
    markdown_content = extract_md_from_pdf(pdf_path)

    # Save to file with same name as PDF but .md extension
    output_path = os.path.splitext(pdf_path)[0] + ".md"
    with open(output_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)
    print(f"PDF converted to Markdown and saved to {output_path}")

__all__ = [extract_md_from_pdf]