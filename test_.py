import os
import wget

URL = "https://github.com/Abacatinhos/agenda-tech-brasil/blob/main/README.md"

OUTPUT_FILE = "file"


def get_readme_file() -> str:
    """get readme from github repo"""

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    readfile = wget.download(URL, OUTPUT_FILE)

    with open('file.json') as user_file:
        file_contents = user_file.read()


    return print(file_contents)

#get_readme_file()

readfile = wget.download(URL, OUTPUT_FILE)
print(readfile)