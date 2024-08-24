import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.question_answering import load_qa_chain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from RAG.extractor import extract_document

load_dotenv()
apiSecret = os.getenv("GROQ_API_SECRET")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Initialise Pinecone VDB
index_name = "ct-docs"

# Retrieve Documents / Chunks
chunks = extract_document(filePath="../data/2022-commercetools-resiliency.pdf")

# Create embeddings
embeddings = OllamaEmbeddings(model="llama3")

# Initialise LLM
llm = ChatGroq(temperature=0.1, model="llama3-70b-8192", api_key=apiSecret)

# Create the vector store
#vector_store = PineconeVectorStore.from_documents(documents=chunks, index_name=index_name, embedding=embeddings)
vector_store = PineconeVectorStore(index_name=index_name, embedding=embeddings)
if vector_store:
    print("Vector Store Created")


def generate_response(question):
    try:
        if question:
            print(f"""Question is here :- {question}""")
            match = vector_store.similarity_search(question)
            chain = load_qa_chain(llm, chain_type="stuff", verbose=True)
            response = chain.invoke(input={"input_documents": match, "question": question})
            print(response)
            return response
    except Exception as ex:
        print(ex)


__all__ = [
    generate_response
]
