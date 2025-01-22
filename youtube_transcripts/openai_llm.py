from dotenv import  load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize OpenAI LLM
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini", verbose=True, stream_usage=True)

__all__ = [llm]