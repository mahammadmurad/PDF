#watermarkadd

import PyPDF2

template = PyPDF2.PdfReader(open('super.pdf' , 'rb'))
watermRK = PyPDF2.PdfReader(open('Wm.pdf' , 'rb'))
output = PyPDF2.PdfFileWriter

for i in range (len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermRK.pages[0])
    output.addPage(page)

with open('wm_output.pdf' , 'wb') as  file :
    output.write(file)
