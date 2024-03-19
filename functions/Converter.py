from pdf2docx import Converter
from docx2pdf import convert

def convert_docx_to_pdf_file(docx_Path):
    error = ''
    pdf_path = ''
    if docx_Path.endswith('.doc') or docx_Path.endswith('.docx'):
        pdf_path = f"{docx_Path.rsplit('.', 1)[0]}.pdf"
        convert_docx_to_pdf(docx_Path, pdf_path)
    else:
        error = 'File is not in the expected format. Expects .docx or .doc'
    return[error, pdf_path]
        


def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

def convert_docx_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)