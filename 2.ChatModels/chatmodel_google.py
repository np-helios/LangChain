from langchain_google_genai import ChatGoogleGenerativeAI as ChatGoogle
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogle(model="gemini-1.5-pro", temperature=0.2, max_output_tokens=100)

result = model.invoke("What is Youtube?")

print(result.content)