import streamlit as st

# Page Title
st.set_page_config(page_title="My Portfolio", layout="centered")

st.title("👨‍💻 Welcome to My Portfolio")
st.subheader("Hello, I'm an aspiring Python developer!")

# About Section
st.header("📌 About Me")
st.write("""
Hi! I'm learning Python and building cool projects.  
I love exploring technology, automation, and data.  
Currently enrolled in the AI-101 course.
""")

# Skills Section
st.header("🛠️ Skills")
st.write("""
- Python  
- HTML & CSS  
- JavaScript  
- Streamlit  
- AI Basics
""")

# Projects Section
st.header("📁 Projects")
st.markdown("- [BMI Calculator](#)")
st.markdown("- [QR Code Generator](#)")
st.markdown("- [Guess the Number Game](#)")

# Contact Section
st.header("📬 Contact Me")
st.write("Email: your_email@example.com")
st.write("GitHub: [yourgithub](https://github.com)")
st.write("LinkedIn: [yourlinkedin](https://linkedin.com)")

st.success("Thanks for visiting my site!")
