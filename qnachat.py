from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="QNA Chat", page_icon=":robot_face:")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

input = st.text_input("Ask a question:", key="input")
submit_button = st.button("Submit", key="submit")
if submit_button and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot", chunk.text))

st.subheader("Chat History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")