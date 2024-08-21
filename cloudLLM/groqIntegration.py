import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from outputParser import output_parser
from LinkedIn_Scraping import linkedIn

load_dotenv()
apiSecret = os.getenv("GROQ_API_SECRET")
template = """ Answer the {question} based on the following {data} in the following format {format}"""
prompt = PromptTemplate(
    input_variables=["question"],
    template=template,
    partial_variables={
        "format": output_parser.get_format_instructions()
    }
)

llm = ChatGroq(temperature=0, model="llama3-70b-8192", api_key=apiSecret)

chain = prompt | llm | output_parser

data = linkedIn.scrape_linkedin_profile(..., True)
response = chain.invoke(
    {"question": "", "data": data}
)
print(response)

__all__ = [llm]
