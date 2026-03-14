import streamlit as st
from agent import ai_agent

st.title("🚀 Binance Campaign Hunter AI")

question = st.text_input("Ask about Binance campaigns:")

if question:
    answer = ai_agent(question)
    st.write(answer)