import json
from typing import Union, List

from dotenv import load_dotenv
from langchain.agents import tool
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.prompts import PromptTemplate
from langchain.tools.render import render_text_description
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from cloudLLM.GroqLLM import groq_llm
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.tools import Tool
from callbacks import AgentCallbackHandler

load_dotenv()

@tool()
def get_text_length(text: str):
    """Returns the length of a text by characters"""
    text = text.strip("\n").strip('"')
    return len(text)


def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"""Could not find tool with name {tool_name}""")


if __name__ == "__main__":
    tools = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought: {agent_scratchpad}
    """

    # Use render_text_description on tools object as LLMs only accepts string as input
    prompt_template = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools), tool_names=",".join(t.name for t in tools)
    )

    # Assigning stop to stop sequences on finding the particular value
    groq_llm.stop = ["\nObservation"]
    groq_llm.callbacks=[AgentCallbackHandler()]
    llm = groq_llm
    intermediate_steps = []
    agent = {"input": lambda x: x["input"], "agent_scratchpad": lambda x: format_log_to_str(
        x["agent_scratchpad"])} | prompt_template | llm | ReActSingleInputOutputParser()

    agent_step = ""
    while not isinstance(agent_step, AgentFinish):
        agent_step: Union[AgentAction, AgentFinish] = agent.invoke(
            {"input": "What is the length of 'DOG' in characters", "agent_scratchpad": intermediate_steps})

        # Agent
        # step - --->
        # tool = 'get_text_length'
        # tool_input = "'DOG'"
        # log = "Let's get started.\n\nThought: I need to find the length of the text 'DOG' in characters.\n\nAction: get_text_length\nAction Input: 'DOG'"
        # print(f"""Agent step ----> \n {agent_step}""")

        if isinstance(agent_step, AgentAction):
            tool_name = agent_step.tool
            tool_to_use: Tool = find_tool_by_name(tools, tool_name)
            tool_input = agent_step.tool_input.strip("\n").strip("'")

            observation = tool_to_use.func(str(tool_input))
            print(f"This is Agent Action Instance. Details : {agent_step}\n")
            print(f"""{observation=}\n""")
            intermediate_steps.append((agent_step, str(observation)))

    if isinstance(agent_step, AgentFinish):
        print(f"This is Agent Finish Instance. Details : {agent_step}")
