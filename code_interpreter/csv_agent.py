from dotenv import load_dotenv
from langchain import hub
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool

load_dotenv()

csv_agent = create_csv_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    path="./product_reviews.csv",
    verbose=True,
    allow_dangerous_code=True
)

# csv_agent.invoke(
#     input={
#         "input": "How many columns are there in the product_reviews.csv ?"
#     }
# )

# csv_agent.invoke(
#     input={
#         "input": "Which product has the best rating and review among first 200 records. If there are multiple records just return only one random product"
#                  "from the highest rated products"
#     }
# )

__all__ = [
    csv_agent
]
