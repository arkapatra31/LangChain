import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from outputParser import getParser
from LinkedIn_Scraping import linkedIn

load_dotenv()
apiSecret = os.getenv("GROQ_API_SECRET")
template = """ Answer the {question} creatively based on the following {data} in the following format {format}"""

prompt = ChatPromptTemplate.from_template(template)

llm = ChatGroq(temperature=0.1, model="llama3-70b-8192", api_key=apiSecret)

chain = prompt | llm

data = linkedIn.scrape_linkedin_profile(..., True)

response = chain.invoke(
    {"question": "Tell me something about", "data": data, "format": getParser().get_format_instructions()}
)
print(response.content)
