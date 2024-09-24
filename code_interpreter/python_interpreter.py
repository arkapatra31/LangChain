from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool

load_dotenv()

instructions = """You are an agent designed to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the question. 
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """

base_prompt = hub.pull("langchain-ai/react-agent-template")
prompt = base_prompt.partial(instructions=instructions)

tools = [PythonREPLTool()]

python_agent = create_react_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    tools=tools,
    prompt=prompt
)

python_agent_executor = AgentExecutor(agent=python_agent, tools=tools, verbose=True)

# python_agent_executor.invoke(
#     input={
#         "input": """Generate and save inside a folder named generated-qr-codes in the current working directory 2 QRcodes
#                                 that point to these two URLs
#                                 https://www.linkedin.com/in/arkapatra31/,
#                                 https://www.facebook.com/31AKP,
#                                 also name the qrcodes file based on the hostname of the URLS and you have qrcode package installed already."""
#     }
# )

__all__ = [
    python_agent_executor
]