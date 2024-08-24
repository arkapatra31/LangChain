from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter


def convert_text_to_chunks(text: str) -> List[str]:
    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        separators=["/n"]
    )
    chunks: List[str] = textSplitter.split_text(text)
    return chunks

__all__ = [
    convert_text_to_chunks
]