from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

# ✅ Set API keys directly (NOT recommended for production)
os.environ["OPENAI_API_KEY"] = "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"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# ✅ Create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# ✅ Streamlit UI
st.title('🤖 Langchain Demo with OpenAI API')
input_text = st.text_input("🔎 Ask me anything")

# ✅ Set up OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# ✅ Run chain if user input is provided
if input_text:
    response = chain.invoke({"question": input_text})
    st.write("🧠 Response:")
    st.success(response)
