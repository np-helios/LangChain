from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
chat_history = [
    SystemMessage(content="You are a helpfull assistant.")
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        # print("AI:Goodbye!")
        break 
    else:
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))
        print(f"AI: {response.content}")
print(chat_history)