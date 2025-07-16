import re
import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]
def is_valid_email(email):
    # Basic Regex Pattern for Email Validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form('contact_form'):
        firstname = st.text_input('First Name')
        lastname = st.text_input('Last Name')
        email = st.text_input('Email Address')
        message = st.text_area('Your Message')
        submit_button = st.form_submit_button('Submit')

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not setup. Please try again later.", icon="📩")
                st.stop()

            if not firstname or not lastname:
                st.error("Please provide your name.", icon="🙎")
                st.stop()

            if not email:
                st.error("Please provide your email address.", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon="📥")
                st.stop()

            if not message:
                st.error("Please provide your message.", icon="💬")
                st.stop()

            #prepare the data payload and send it to the specified webhook url
            data = {"First Name": firstname, "Last Name": lastname, "Email": email, "Message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully.! 🎉", icon="🚀")

            else:
                st.error("There was an error sending your message.", icon="😫")
