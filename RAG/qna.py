import os

from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS, InMemoryVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
apiSecret = os.getenv("GROQ_API_SECRET")
question = "What is continued resilency?"

text = ""
file = open('../docs/2022-commercetools-resiliency.pdf', 'rb+')
if file is not None:
    print("File exists")
    pdfReader = PdfReader(file)

    for x in range(len(pdfReader.pages)):
        page = pdfReader.pages[x]
        text += page.extract_text()
    if text is not None:
        print("Text Extracted")

    text_splitter = RecursiveCharacterTextSplitter(
        length_function=len,
        separators=["\n"],
        chunk_size=150,
        chunk_overlap=100
    )

    # Split the entire content into chunks
    chunks = text_splitter.split_text(text)

    if chunks is not None:
        print(f''' Text Splitted into {len(chunks)} chunks''')

    # Create embeddings
    embeddings = OllamaEmbeddings(model="llama3")

    # Initialise LLM
    llm = ChatGroq(temperature=0.1, model="llama3-70b-8192", api_key=apiSecret)

    print("Embedding and LLM Initialised")

    # Create the vector store
    vector_store = InMemoryVectorStore.from_texts(chunks, embeddings)

    if vector_store:
        print("Vector Store Created")
        print(vector_store)

    if question:
        print("Question is there")
        match = vector_store.similarity_search(question)
        print(match)

        chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
        response = chain.invoke(input_documents=match, question=question)
        print(response)
