from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation",
    max_new_tokens=50,
    provider="together",
)

# Test 1: Non-streaming (_call) — should work
print("Testing non-streaming...")
result = llm.invoke("What is 2+2?")
print(f"Non-streaming result: {result}")

# Test 2: Streaming (_stream) — this is where the bug is
print("\nTesting streaming...")
for chunk in llm.stream("What is 2+2?"):
    print(chunk, end="", flush=True)
print()