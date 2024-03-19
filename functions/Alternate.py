import win32com.client
import os

# INPUT/OUTPUT PATH
pdf_path = r"C:\Users\P.Bhaskaran\Downloads\[Template Form] Power of attorney Non-EU - Telescope Services AB (use) (2) (1) (3) (1) (3) (1) (1) (2) (1) (1) (1).pdf"
output_path = r"C:\Users\P.Bhaskaran\Downloads"

word = win32com.client.Dispatch("Word.Application")
word.visible = 1  # CHANGE TO 1 IF YOU WANT TO SEE WORD APPLICATION RUNNING AND ALL MESSAGES OR WARNINGS SHOWN BY WORD

# GET FILE NAME AND NORMALIZED PATH
filename = pdf_path.split('\\')[-1]
in_file = os.path.abspath(pdf_path)

# CONVERT PDF TO DOCX AND SAVE IT ON THE OUTPUT PATH WITH THE SAME INPUT FILE NAME
wb = word.Documents.Open(in_file)
out_file = os.path.abspath(output_path + '\\' + filename[0:-4] + ".docx")
wb.SaveAs2(out_file, FileFormat=16)
wb.Close()
word.Quit()