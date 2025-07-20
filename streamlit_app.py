import streamlit as st
import os
from parser import get_resume_text
from analyser import calculate_match_score

st.title("AI Resume Analyser")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description")

if uploaded_file and job_desc:
    file_extension = os.path.splitext(uploaded_file.name)[1]  # get .pdf or .docx
    temp_filename = f"temp_resume{file_extension}"

    with open(temp_filename, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        resume_text = get_resume_text(temp_filename)
        score = calculate_match_score(resume_text, job_desc)
        st.success(f"Resume Match Score: {score}%")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
