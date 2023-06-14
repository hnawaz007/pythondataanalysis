import streamlit as st 
from gpt4all import GPT4All

gpt = GPT4All("ggml-gpt4all-l13b-snoozy.bin")

#
st.title(' GPT For All')
prompt = st.text_input('Enter your prompt here!')

messages = [{"role": "user", "content": prompt}]
#



if prompt: 
    try:
        response = gpt.chat_completion(messages)
        st.write(response['choices'][0]['message']['content'])
    except ValueError as e:
        st.write(e)
        
		
