import PyPDF2
import os


def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text



# def convert_folder_to_text(folder_path):
#     text_files = []
#     for filename in os.listdir(folder_path):
#         print(f"Converting {filename}....")
#         if filename.endswith(".pdf"):
#             pdf_path = os.path.join(folder_path, filename)
#             text = pdf_to_text(pdf_path)
#             text_files.append((filename, text))
#     return text_files

# folder_path = "List of Acts\\New\\CENTRAL ACT LEGISLATION"
#converted_texts = convert_folder_to_text(folder_path)


def convert_folder(folder_path):
    text_files = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".pdf"):
                pdf_path = os.path.join(root, file_name)
                text = pdf_to_text(pdf_path)
                text_files.append((root, text))
    return text_files




start_year = 1949
end_year = 2020
output_folder = "folder_converted" 

line = "-" * 26

for year in range(start_year, end_year):
    print("Converting folder: ", year)
    folders_path = f"List of Acts\\{year}"
    convert_folders = convert_folder(folders_path)
    

    output_file = os.path.join(output_folder, f"{year}.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for folder_name, text in convert_folders:
            parts = str(folder_name).split("\\")
            result = parts[-1]
            f.write(f"{line}{result}{line}\n{text}\n")