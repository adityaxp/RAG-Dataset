import os

folder_path = "folder_converted"

output_file_path = "RAG-Input.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as input_file:
                file_contents = input_file.read()
                output_file.write(file_contents)
                output_file.write("\n")
