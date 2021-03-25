input=r"C:/Users/ykris/Desktop/1.docx"
output=r"C:/Users/ykris/Desktop/1.pdf"
folder="C:/Users/ykris/Desktop/samp"
from docx2pdf import convert
def pdftoword(input,output,folder):
      convert(input)
      convert(input,output)
      convert(folder)

      return pdftoword()