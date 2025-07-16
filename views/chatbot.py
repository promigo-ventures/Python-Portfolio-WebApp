import random
import time
import streamlit as st

def response_generator():
    response = random.choice(
        [
            "What is your name?: Promise Godwin",
            "How can i see projects you've worked on?: Check my project tab at the left side corner of my navigation bar",
            "How can i get in touch with you?: You can reach out to me through the contact form in my about me page"
        ]
    )
    for word in response.split():
        yield word + ""
        time.sleep(0.05)

st.title("Chatbot")

#Initialize Chat History
if "messages"not in st.session_state:
    st.session_state.messages = []

#Display chat messages from history on   app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Accept user input
if prompt := st.chat_input("What is up?"):
    #Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    #Display user message in that message container
    with st.chat_message("user"):
        st.markdown(prompt)

    #Display assistant response to chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    #Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})





















