from dotenv import load_dotenv
import os
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import OllamaEmbeddings
from youtube_transcripts import llm, export_transcript_text
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

path = "../summarizer/long_video/transcript.txt"
transcript = export_transcript_text(path)

pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_index = "youtube-transcripts"
try:

    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=0,
        length_function=len,
        keep_separator=True,
        separators=["", "\n"]
    )

    chunks = textSplitter.split_text(transcript)

    embeddings = OllamaEmbeddings(model="llama3:latest", num_gpu=1)

    # Create new Pinecone Vector Store
    vector_store = PineconeVectorStore.from_texts(
        index_name=pinecone_index,
        embedding=embeddings,
        texts=chunks
    )

    print("Pinecone Vector Store Created")

except Exception as e:
    print(f"Error: {e}")
