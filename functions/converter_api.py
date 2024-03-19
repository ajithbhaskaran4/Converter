from flask import Flask, request, jsonify
from Converter import convert_pdf_to_docx, convert_docx_to_pdf

app = Flask(__name__)

@app.route('/convert_pdf_2_docx', methods=['POST'])
def convert_pdf_to_docx():
    try:
        # Check if a file is included in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # Check if the file has a name and it has a PDF extension
        if file.filename == '' or not file.filename.lower().endswith('.docx') or not file.filename.lower().endswith('.doc'):
            return jsonify({'error': 'Invalid file'}), 400

        # Convert PDF to DOCX
        pdf_path = file.filename
        docx_path = f"{file.filename.rsplit('.', 1)[0]}.docx"

        convert_pdf_to_docx(pdf_path, docx_path)

        return jsonify({'result': 'success', 'docx_path': docx_path})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/convert_docx_2_pdf', methods=['POST'])
def convert_docx_to_pdf():
    try:
        # Check if a file is included in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # Check if the file has a name and it has a PDF extension
        if file.filename == '' or not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'Invalid file'}), 400

        # Convert DOCX to pdf
        docx_path = file.filename
        pdf_path = f"{file.filename.rsplit('.', 1)[0]}.pdf"

        convert_docx_to_pdf(docx_path, pdf_path)

        return jsonify({'result': 'success', 'pdf_path': pdf_path})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
