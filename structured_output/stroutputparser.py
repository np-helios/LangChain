from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template="Give a detailed report on {topic}?",
    input_variables= ['topic']
)
template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text. /n {text}",
    input_variables = ['text']
)

prompt1 = template1.format(topic="Black Holes")
result = model.invoke(prompt1)

prompt2 = template2.format(text = result.content)

result2 = model.invoke(prompt2)

print(result2.content)