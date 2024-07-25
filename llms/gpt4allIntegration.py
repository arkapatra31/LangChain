from langchain_community.llms import GPT4All
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.callbacks import BaseCallbackHandler

count = 0
class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        global count
        if count < 10:
            print(f"Token: {token}")
            count += 1


template = """ Summarize the following Youtube video {URL} in 5 pointers - {topic} """

prompt = ChatPromptTemplate.from_template(template)

llm = GPT4All(
    model="../gpt4all_LLMs/Meta-Llama-3.1-8B-Instruct.Q4_0.gguf",
    backend = "llama"
    #callbacks=[MyCustomHandler()],
    #streaming=True,
)

chain = prompt | llm

answer = chain.invoke({"URL": "https://www.youtube.com/watch?v=p5j291G-Wvo"})
