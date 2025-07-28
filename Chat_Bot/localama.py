from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama  # ✅ Correct class import

import streamlit as st
import os 
from dotenv import load_dotenv

# Load .env file if needed
load_dotenv()

# Set API keys (OpenAI and LangChain)
os.environ["OPENAI_API_KEY"] = "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"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title('🤖 Langchain Demo with Ollama (LLaMA2)')
input_text = st.text_input("🔎 Ask me anything")

# ✅ Instantiate the Ollama LLM correctly
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run the chain
if input_text:
    response = chain.invoke({"question": input_text})
    st.write("🧠 Response:")
    st.success(response)