from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class GeminiLLM():
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro-002",
            temperature=0,
            verbose=True,
            transport="rest"
            #max_output_tokens= 9999
        )

    def returnLLMInstance(self):
        return self.llm

gemini_llm = GeminiLLM().returnLLMInstance()

__all__ = [
    gemini_llm
]
