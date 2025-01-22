from langchain.chains.combine_documents import create_stuff_documents_chain
from youtube_transcripts import llm
from langchain import hub
from langchain_community.embeddings import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains.retrieval import create_retrieval_chain


#pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index = "youtube-transcripts"

# Pull the prompt for qa-chain from LangChain Hub
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

# Initialise Embeddings
embeddings = OllamaEmbeddings(model="llama3:latest")

# Intialise vector store
vector_store = PineconeVectorStore(index_name=pinecone_index, embedding=embeddings)

# Create the chain of type document stuff
combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

# Create the Retrieval Chain
retrieval_chain = create_retrieval_chain(
    retriever=vector_store.as_retriever(), combine_docs_chain=combine_docs_chain
)

__all__ = [
    retrieval_chain
]
