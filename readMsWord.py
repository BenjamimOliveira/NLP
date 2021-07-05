# packages necessários:
# -- pip install python-docx 
from docx import Document

filename = "data/file-sample.docx"

# Carregar o doc Word
doc = open(filename, "rb")

# Criar Word reader
document = Document(doc)

# String vazia. Esta string vai guardar paragrafo a paragrafo
docu = ""
for para in document.paragraphs:
    docu += para.text

# Resultado final
print(docu)