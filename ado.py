import json
import os
import shutil

def importExtensions():
    with open('file_extensions.json', 'r') as ext_file:
        data = json.load(ext_file)
    
    return data

def testDirectory(name):
    if not os.path.isdir(name):
        os.mkdir(name)

def testExtension(extension, data):
    for i in range(len(data)):
        if extension in data[i]["extensions"]:
            testDirectory(data[i]["name"])
            return data[i]["name"]

def main():
    current_files = os.listdir()

    print("akim's Directory Organizer")

    extension_data = importExtensions()

    for i in range(len(current_files)):
        root, extension = os.path.splitext(current_files[i])

        if not extension:
            continue

        new_dir = testExtension(extension, extension_data)
        shutil.move(current_files[i], new_dir)


if __name__ == "__main__":
    main()
