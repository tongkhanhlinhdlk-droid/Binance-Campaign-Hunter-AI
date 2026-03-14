import streamlit as st
from agent import ai_agent

st.title("Binance Campaign Hunter AI")

user_input = st.text_input("Ask about Binance campaigns:")

if user_input:
    response = ai_agent(user_input)
    st.write(response)
