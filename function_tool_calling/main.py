import os
from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.tools import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def multiply(x: int, y: int) -> int:
    """Returns the multiplication of x and y from input parameters"""
    return x * y


if __name__ == '__main__':
    print("***************** TOOL Calling *****************")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}")
        ]
    )

    tools = [
        TavilySearchResults(), multiply
    ]

    llm1 = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    #llm1.bind_tools(tools=tools)

    llm2 = ChatGroq(temperature=0, model="llama3-70b-8192", api_key=os.getenv('GROQ_API_SECRET'))

    #llm2.bind_tools(tools=tools)

    agent1 = create_tool_calling_agent(llm=llm1, tools=tools, prompt=prompt)

    agent2 = create_tool_calling_agent(llm=llm2, tools=tools, prompt=prompt)

    agent_executor1 = AgentExecutor(agent=agent1, tools=tools, verbose=True)
    agent_executor2 = AgentExecutor(agent=agent2, tools=tools, verbose=True)

    response1 = agent_executor1.invoke(
        {
            "input": "What is the weather in Kolkata right now ? Also compare it with Delhi and output should be in Celsius"
        }
    )

    response2 = agent_executor2.invoke(
        {
            "input": "What is 5*2? Even if you know the answer, then also use the tool to calculate the answer and return the same"
        }
    )

    print(f"{response1=}\n{response2=}")
