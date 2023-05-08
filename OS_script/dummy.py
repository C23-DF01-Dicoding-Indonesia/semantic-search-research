# delete all markdown file in data


import os
from pyprojroot.here import here

def delete_all_markdown_files(folder):
    """
    Deletes all markdown files in a folder.
    folder: a string of the folder path
    """
    for file in os.listdir(folder):
        os.remove(os.path.join(folder, file))


if __name__ == "__main__":
    delete_all_markdown_files(here("data"))
