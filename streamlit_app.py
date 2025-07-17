import streamlit as st

#PAGE SETUP
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)

project_1_page = st.Page(
    page='views/sales_dashboard.py',
    title='Sales Dashboard',
    icon=':material/bar_chart:',
)

project_2_page = st.Page(
    page='views/chatbot.py',
    title='Chat Bot',
    icon=':material/smart_toy:',
)

st.header("Promise Godwin's Portfolio", anchor=False)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#NAVIGATION SETUP
pg = st.navigation({
     'Info': [about_page],
     'Projects': [project_1_page, project_2_page]
     })

#SHARED ON ALL PAGES
st.logo('assets/1.png')
st.sidebar.text("Made with ♥️ by Promise Godwin")

#RUN NAVIGATION
pg.run()


