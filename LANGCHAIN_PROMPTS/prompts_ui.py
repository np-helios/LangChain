from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, max_tokens=1000)
st.header("Research Paper Summarizer")

paper_input = st.selectbox("Select a research paper", ["Attenton is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners"])

style_input = st.selectbox("Select a summary style", ["Beginner-Friendly", "Technical", "Concise"])

length_input = st.selectbox("Select summary length", ["Short (1-2 sentences)", "Medium (3-5 sentences)", "Long (6-10 sentences)"])

template = PromptTemplate(
    template="""Please sumnarize the research paper titled:{paper_input} with the following
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
- Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing-
Ensure the summary is clear, accurate, and aligned with the provided style and length requirements."""
, input_variables=["paper_input", "style_input", "length_input"]
)

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("Generate Summary"):
    result = model.invoke(prompt)
    st.write(result.content)