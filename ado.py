import json
import os

def main():
    current_files = os.listdir()

    print("akim's Directory Organizer")

    for i in range(len(current_files)):
        root, extension = os.path.splitext(current_files[i])

        if not extension:
            continue



if __name__ == "__main__":
    main()
