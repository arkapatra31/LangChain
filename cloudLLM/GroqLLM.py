import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_SECRET")

groq_llm = ChatGroq(temperature=0, model="llama3-8b-8192", api_key=groq_api_key)

__all__ = [
    groq_llm
]
