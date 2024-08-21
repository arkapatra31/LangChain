import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools import get_profile_tavily

load_dotenv()
apiSecret = os.getenv("GROQ_API_SECRET")


def lookup(name: str):
    template = """Given the full name {name_of_person} I want you to get me some information about their LinkedIn profile.
    Your answer should be specific, detailed and in JSON format"""

    llm = ChatGroq(temperature=0, model="llama3-70b-8192", api_key=apiSecret)

    # Initialise Template
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    # Initialise Agent Tool
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_tavily,
            description="Useful for when you need to get LinkedIn Profile Information"
        )
    ]

    # Initialise the ReAct Prompt
    react_prompt = hub.pull("hwchase17/react")

    # Create the ReAct Agent
    react_agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    # Create Agent Executor
    agent_executor = AgentExecutor(agent=react_agent, tools=tools_for_agent, verbose=True)

    # Invoke the agent executor
    result = agent_executor.invoke(
        input={
            "input": prompt_template.format_prompt(name_of_person=name)
        }
    )

    response = result["output"]
    return response


if __name__ == '__main__':
    lookup(name="Harrison Chase")
