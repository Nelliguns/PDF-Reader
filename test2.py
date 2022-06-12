from PyPDF4 import PdfFileReader
from pathlib import Path


pdf = PdfFileReader('curriculum.pdf')

page_1_object = pdf.getPage(0)  # Note pages are indexed

# extract text
page_1_text = page_1_object.extractText()

with Path("curriculum_text.txt").open(mode="w") as output_file:
    text = ""
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)

