from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary: str 
    sentiment: str

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("The movie was fantastic! I loved the storyline and the acting was superb.")
print(result)