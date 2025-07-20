import pdfplumber
import docx

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return ' '.join(page.extract_text() or '' for page in pdf.pages)

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return ' '.join([p.text for p in doc.paragraphs])

def get_resume_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
