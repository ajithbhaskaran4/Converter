import streamlit as st
import tempfile
import os
from functions import Converter

if 'tempDir' not in st.session_state:
    st.session_state.tempDir = tempfile.mkdtemp()
if 'filePath' not in st.session_state:
       st.session_state.filePath = ""

st.title("Convert your Docx to PDF")

uploaded_file = st.file_uploader("Choose a docx/doc file", accept_multiple_files=False)
if uploaded_file:
        st.session_state.filePath = os.path.join(st.session_state.tempDir, uploaded_file.name)
        with open(st.session_state.filePath, "wb") as f:
                f.write(uploaded_file.getvalue())
    
if st.button('SUBMIT'):
    [error, pdf_Path] = Converter.convert_docx_to_pdf_file(st.session_state.filePath)
    print("PDF Path :", pdf_Path)
    if error == '':
        with open(pdf_Path, 'rb') as f:
            st.download_button('Download Your PDF', f, file_name=os.path.split(pdf_Path)[-1])
        
