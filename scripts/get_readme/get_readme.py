import os
import wget

URL = "https://raw.githubusercontent.com/Abacatinhos/agenda-tech-brasil/refs/heads/main/src/db/database.json"

OUTPUT_FILE = "file.json"


def get_readme_file() -> str:
    """get readme from github repo"""

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    readfile = wget.download(URL, OUTPUT_FILE)

    with open('file.json') as user_file:
        file_contents = user_file.read()


    return file_contents

