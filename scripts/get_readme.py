import os
import wget

URL = "https://raw.githubusercontent.com/Abacatinhos/agenda-tech-brasil/refs/heads/main/README.md"

OUTPUT_FILE = "file.md"


def get_readme_file() -> str:
    """get readme from github repo"""

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    readfile = wget.download(URL, OUTPUT_FILE)
    f = open(readfile)
    r = f.read()

    return r


get_readme_file()
