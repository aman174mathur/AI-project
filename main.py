from parser import get_resume_text
from analyser import calculate_match_score

# Load job description
with open('job_description.txt', 'r') as f:
    job_desc = f.read()

# Test with sample resume
resume_file = 'resume_samples/resume1.pdf'  # or .docx
resume_text = get_resume_text(resume_file)

score = calculate_match_score(resume_text, job_desc)

print(f"Match Score with Job Description: {score}%")
