from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import pandas as pd
from langchain.prompts import PromptTemplate

load_dotenv()

# Initialize ChatOpenAI
llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini", verbose=True)

__all__ = [llm]
