import json
import os

def importExtensions():
    with open('file_extensions.json', 'r') as ext_file:
        data = json.load(ext_file)
        print(data)

def main():
    current_files = os.listdir()

    print("akim's Directory Organizer")

    for i in range(len(current_files)):
        root, extension = os.path.splitext(current_files[i])

        if not extension:
            continue

        importExtensions()



if __name__ == "__main__":
    main()
