from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize ChatOpenAI
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", verbose=True)

__all__ = [llm]
