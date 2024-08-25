from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter, TokenTextSplitter


def convert_text_to_chunks(text: str) -> List[str]:
    textSplitter = RecursiveCharacterTextSplitter(#TokenTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        #length_function=len,
        #separators=[""]
    )
    chunks: List[str] = textSplitter.split_text(text)
    return chunks


__all__ = [
    convert_text_to_chunks
]
