from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv 

load_dotenv()

model = ChatAnthropic(model="claude-2", temperature=0.2, max_completion_token = 10)
result = model.invoke("What is the capital of India")

print(result.content)