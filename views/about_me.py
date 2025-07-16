import streamlit as st
from forms.contact import contact_form

@st.dialog('Contact Me')
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/WhatsApp Image 2025-07-15 at 9.29.23 PM.jpeg", width=280)
with col2:
    st.title("Promise Godwin", anchor=False)
    st.write(
        "Experienced Robotics and Coding Engineer, Software Engineer and Data Analyst."
    )
    if st.button('📩 Contact Me'):
        show_contact_form()

#Experience & Qualifications
st.write('\n')
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
- Robotics & Coding Engineer, Nigenius
Developed and taught robotics, C++, Python, AI, and RPA to students (Aug 2024 – Present)

- Director & Operations Manager, Today's Exclusive Hotel
Led operations, HR, finance, and maintenance across multiple roles (Apr 2023 – Present)

- Senior Manager, Business Operations, Promigo Ventures
Oversaw business strategy, digital transformation, and social media (Jan 2021 – Present)

- Chemistry Lecturer (NYSC), Plateau State College of Nursing and Midwifery
Taught and mentored chemistry students; organized assessments (Nov 2019 – Dec 2020)

- Video Editor Intern, MRT Academy
Hands-on video editing experience (Jun 2020 – Oct 2020)

- Digital Marketer, Martnextdoor GS Ltd
SEO, content creation, graphic design, and campaign management (May 2019 – Aug 2019)

- Quality Assurance Intern, CHI Limited
Lab testing and production QA for consumer products (Jan 2018 – Jul 2018)
    """
)

st.write('\n')
st.subheader('Hard Skills', anchor=False)
st.write("""

- Programming Languages: Python, Java, C++, C

- Web Development: React.js, HTML, CSS, JavaScript, React, 

- Backend Development: Node.js, Express.js 

- Database Tools & Analytics: SQL, Tableau, Google Analytics, MongoDB

- Data Visualization: PowerBI, MS Excel

- AI & Automation: Machine Learning, Generative AI, RPA

- Content & Media: Canva, Video Editing

- Software Proficiency: Microsoft Office Suite

- Other Skills: SEO, Digital Marketing, Graphic Design, Project Management, Teaching & Training
""")

st.write('\n')
st.subheader('Education Background', anchor=False)
st.write("""
- B.Sc. Industrial Chemistry, Landmark University, Kwara State
""")

st.write('\n')
st.subheader('Certifications', anchor=False)
st.write("""
- Robotics, AI & ML, RPA, Digital Marketing, Business Process Management, 
HSE, Entrepreneurship, and more (30+ certifications)
""")