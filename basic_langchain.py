import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY') # getpass.getpass()

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(content="Translate the following from English into Portuguese"),
    HumanMessage(content="hi!"),
]

ai_message = model.invoke(messages)

print(ai_message.content)
