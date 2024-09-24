from dotenv import load_dotenv
from typing import Any, Dict
from langchain import hub
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from code_interpreter.python_interpreter import python_agent_executor
from code_interpreter.csv_agent import csv_agent

load_dotenv()


def main():

    def python_agent_executor_wrapper(original_propmt: str) -> Dict[str, Any]:
        return python_agent_executor.invoke({"input": original_propmt})

    tools = [
        Tool(
            name="PYTHON AGENT",
            func=python_agent_executor_wrapper,
            description="""Useful when you need to transform natural language to python and execute the python code,
            returning the results of the code execution
            DOES not accept Code as INPUT"""
        ),
        Tool(
            name="CSV AGENT",
            func=csv_agent.invoke,
            description="""Useful when you need to answer questions related to the products_reviews.csv file,
            takes an input the entire question and returns the answer after running the pandas calculations"""
        )
    ]

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions="")

    grand_agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        tools=tools
    )

    grand_agent_executor = AgentExecutor(agent=grand_agent, tools=tools, verbose=True)

    # grand_agent_executor.invoke(
    #     input={
    #         "input": "Which is the most repetetive product in the product_reviews.csv? Return only the name"
    #     }
    # )

    grand_agent_executor.invoke(
        input={
            "input": """Generate and save in the current working directory a QR code,
             that point to this https://www.linkedin.com/in/arkapatra31/,
             and you have qrcode package installed already."""
        }
    )


if __name__ == '__main__':
    main()
