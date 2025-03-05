import PyPDF2
import os

FOLDER_OUT = 'merged'

merger = PyPDF2.PdfMerger()
file_name = ''

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        new_file_name = file.replace('.pdf', '')

        if file_name == '':
            file_name = new_file_name

        else:
            file_name += f'_{new_file_name}'

        merger.append(file)

merged_file_path = os.path.join(os.curdir, FOLDER_OUT, f'{file_name}.pdf')
merger.write(merged_file_path)
