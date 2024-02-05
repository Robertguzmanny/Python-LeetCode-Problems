import os
import shutil
import os.path


# def uniquify(path):
#     filename, extension = os.path.splitext(path)
#     counter = 1
#
#     while os.path.exists(path):
#         path = filename + " (" + str(counter) + ")" + extension
#         counter += 1
#
#     return path




def auto_pdf():
    downloads_folder = os.path.expanduser("~/Downloads")
    pdf_folder = os.path.expanduser("~/Downloads/PDF_Folder")



    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    for file_name in os.listdir(downloads_folder):
        if file_name.endswith(".PDF") or file_name.endswith(".pdf"):
            file_path = os.path.join(downloads_folder, file_name)
            shutil.move(file_path, pdf_folder)


auto_pdf()

