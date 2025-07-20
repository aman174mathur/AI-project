import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

def calculate_match_score(resume_text, job_desc):
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_desc)

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([cleaned_resume, cleaned_jd])

    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(score[0][0]) * 100, 2)  # return percentage
