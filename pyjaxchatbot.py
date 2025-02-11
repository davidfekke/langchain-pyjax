import os
import streamlit as st
from openai import OpenAI

openai_api_key = os.getenv('OPENAI_API_KEY')

st.title("💬 PyJax Chatbot")

# Create a selection tool that will let the streamlit user choose the model they want to use between gpt-4.0 or o1-mini
model = st.selectbox("Select a model", ["gpt-4o", "gpt-4o-mini", "o1-mini"])

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # previous model was gpt-3.5-turbo
    response = client.chat.completions.create(model=model, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    