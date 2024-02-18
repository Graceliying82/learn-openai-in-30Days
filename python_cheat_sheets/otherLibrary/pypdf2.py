from PyPDF2 import PdfReader
from streamlit import st

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

pdf_docs = st.file_uploader("Upload your pdfs here and click on 'Proces'", accept_multiple_files= True)
raw_text = get_pdf_text(pdf_docs)