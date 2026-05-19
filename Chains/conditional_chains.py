from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, chain

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = " Classify the sentiment of the following feedback text into positive or negative \n Feedback: {feedback}",
    input_variables = ["feedback"]
)
classifier_chain = prompt1 | model | parser 

result = classifier_chain.invoke({'feedback': "The product is amazing and the customer service was excellent!"})

print(result)