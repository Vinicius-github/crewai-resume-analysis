from scr.extract_text_from_pdf import extract_text_from_pdf
from scr.extract_text_from_docx import extract_text_from_docx

def extract_text_from_resume(file_path):
    """Determines file type and extracts text."""
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file format."