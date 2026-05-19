from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, chain

from dotenv import load_dotenv

load_dotenv()

model_1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
model_2 = ChatOpenAI(model="gpt-4", temperature=0.9)

prompt_1 = PromptTemplate(
    template = "Write a short and simple summary on the {topic}",
    input_variables = ["topic"]
)

prompt_2 = PromptTemplate(
    template = "Generate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt_3 = PromptTemplate(
    template = "Merge the provided notes and quiz into a single document.\n Notes: {notes} and Quiz: {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

Parallel_chain = RunnableParallel({
    "notes": prompt_1 | model_1 | parser ,
    "quiz": prompt_2 | model_2 | parser
})

final_chain = Parallel_chain | prompt_3 | model_1 | parser
result = final_chain.invoke("Artificial Intelligence")
print(result)

final_chain.get_graph().print_ascii()