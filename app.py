import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")
st.write("Welcome to AI Resume Analyzer!")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    
