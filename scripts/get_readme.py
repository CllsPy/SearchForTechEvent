import wget

PATH = "scripts"


def get_readme_file(url: str) -> str:
    """get readme from github repo"""

    readfile = wget.download(url, PATH)
    f = open(readfile)
    r = f.read()

    return r
