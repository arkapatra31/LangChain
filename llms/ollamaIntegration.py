from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

template = """
    Tell me something about {question} and return me a summary in a JSON body containing QN and ANS key
"""

prompt = ChatPromptTemplate.from_template(template)

llm = Ollama(
    base_url='http://localhost:11434',
    model="llama3:latest"
)

chain = prompt | llm

answer = chain.invoke({"question":"Who is Elon Musk"})
print(answer)