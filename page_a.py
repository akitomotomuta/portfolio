import time
import streamlit as st

def test(prompt):
    print(prompt)
    time.sleep(10)
    return "hello" + prompt

st.title("hello! How can I assist you?")

prompt = st.chat_input("Say something")

if prompt:
    with st.container(height=400):
        with st.spinner('Wait for it...'):
            data = test(prompt)
        st.markdown(data)
        st.write("This is inside the container")