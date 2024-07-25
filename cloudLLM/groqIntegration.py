import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from outputParser import getParser

load_dotenv()
apiSecret = os.getenv("GROQ_API_SECRET")
template = """ Summarize the answer for the following {question} in the following format {format}"""

prompt = ChatPromptTemplate.from_template(template)

llm = ChatGroq(temperature=0, model="llama3-70b-8192", api_key=apiSecret)

chain = prompt | llm

response = chain.invoke(
    {"question": "What is Facebook", "format": getParser().get_format_instructions()}
)
print(response.content)
