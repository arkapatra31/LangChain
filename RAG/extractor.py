from langchain_community.document_loaders import PyPDFLoader


def extract_document(filePath):
    file = PyPDFLoader(file_path=filePath, extract_images=True)
    documents = file.load_and_split()
    return documents


__all__ = [
    extract_document
]
