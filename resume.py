from resume_parser import resumeparse
from pyresparser import ResumeParser
import os
from docx import Document

##file format should be in .txt , .docx or .pdf only
filed='NareshResume.pdf'

try:
    doc = Document()
    with open(filed, 'r') as file:
        doc.add_paragraph(file.read())
    doc.save("text.docx")
    data = ResumeParser('text.docx').get_extracted_data()
    print(data['skills'])
    print(data)
except:
    data = ResumeParser(filed).get_extracted_data()
    print(data['skills'])
    print(data)


#data = resumeparse.read_file('NareshResume.pdf')
#print(data)
