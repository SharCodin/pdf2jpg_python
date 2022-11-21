import os
from tkinter import filedialog
import sys

import fitz


pdf_file = filedialog.askopenfilename(filetypes=[('pdf', '*.pdf')])
if not pdf_file:
    print('Please select a valid file.')
    sys.exit(1)

filename = pdf_file.split('/')[-1].split('.')[0]
directory = os.path.split(pdf_file)[0]
destination_directory = os.path.join(directory, filename)
if not os.path.exists(destination_directory):
    os.mkdir(destination_directory)

doc = fitz.Document(pdf_file)

print(f"\nProcessing file: {filename}")

for page in doc:
    pix = page.get_pixmap() # type: ignore
    page_number = str(page.number).zfill(4)
    print(f"Page: {page_number}", end='\r')
    pix.save(f'{destination_directory}/page_{page_number}.png')

print('\n\r')

sys.exit(0)
