# packages necessários:
# -- pip install PyPDF2
import PyPDF2
from PyPDF2 import PdfFileReader

filename = "data/ata_cm_viana.pdf"

# Criar objeto PDF
pdf = open(filename, "rb")

# Criar PDF Reader
pdf_reader = PyPDF2.PdfFileReader(pdf)

# Verificar número de páginas no ficheiro pdf
print(pdf_reader.numPages)

# Obter apenas umas página
page = pdf_reader.getPage(0)

# Extrair texto da página
print(page.extractText())

# Fechar pdf
pdf.close()