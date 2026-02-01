import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Moses Seabi | Portfolio",
    layout="wide",
    page_icon="👨‍💻"
)

# Load images (replace with your own file paths)
try:
    profile_pic = Image.open("profile-pic.png")  # Your profile picture
    python_logo = Image.open("python-pic.png")  # Python logo
    js_logo = Image.open("pic.png")  # JavaScript logo
    streamlit_logo = Image.open("checkmark.png")  # Streamlit logo
except:
    st.warning("Images not found. Make sure your image files are in the same folder.")

# HEADER
col1, col2 = st.columns([1, 3])
with col1:
    if 'profile_pic' in locals():
        st.image(profile_pic, width=150)
with col2:
    st.title("👋 Moses Seabi")
    st.subheader("Aspiring Software / Web Developer")
    st.write("""
    Welcome to my interactive **Streamlit Portfolio**!
    Explore my skills, projects, and contact info.
    """)

st.markdown("---")

# ABOUT ME
st.header("About Me")
st.write("""
I am a motivated and curious developer with a passion for
building **clean, efficient, and user-friendly applications**.

I enjoy learning new technologies and applying them to solve real-world problems.
""")

st.markdown("---")

# SKILLS
st.header("Skills")
col1, col2, col3 = st.columns(3)

with col1:
    if 'python_logo' in locals():
        st.image(python_logo, width=60)
    st.write("**Python**")

with col2:
    if 'js_logo' in locals():
        st.image(js_logo, width=60)
    st.write("**JavaScript**")

with col3:
    if 'streamlit_logo' in locals():
        st.image(streamlit_logo, width=60)
    st.write("**Streamlit**")

st.write("""
Other skills include:
- HTML & CSS  
- Git & GitHub  
- VS Code  
- Basic SQL
""")

st.markdown("---")

# PROJECTS
st.header("Projects")

st.subheader("Portfolio Website 🌐")
st.write("""
A personal portfolio website showcasing my background, skills, and projects using web technologies.
""")
st.write("🔗 GitHub: [Portfolio](https://github.com/FargoSeabi)")

st.subheader("Streamlit Applications 📊")
st.write("""
Small Python applications built using Streamlit for learning, experimentation, and problem-solving.
""")

st.markdown("---")

# CONTACT
st.header("Contact Me 📫")
col1, col2 = st.columns(2)

with col1:
    st.write("""
    📧 **Email:** moses.seabi@example.com  
    📍 **Location:** South Africa  
    💻 **GitHub:** [FargoSeabi](https://github.com/FargoSeabi)  
    """)

with col2:
    st.write("""
Let's connect and collaborate! I am open to internships, projects, and junior developer opportunities.
""")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")

