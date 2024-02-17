import streamlit as st
import litellm
import random

st.set_page_config(page_title="Chatbot - Powered by Open Source LLM")

## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    #message_placeholder = st.empty()
    full_response = ""
    #messages.append({"role": "user", "content": message.content})
    output =  litellm.completion(
            model="ollama/mistral",
            messages=prompt,
            api_base="http://localhost:11434",
            stream=True
    )
    #
    for chunk in output:
        if chunk:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
         #
    return full_response



st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Ollama & Open Source LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = generate_response(st.session_state.messages)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)