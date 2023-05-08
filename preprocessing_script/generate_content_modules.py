import json
import os
from markdownify import markdownify as md
import re
from pyprojroot.here import here
import re

def remove_code_blocks(markdown):
    """
    Removes all code blocks from a markdown string.
    markdown: a string of markdown
    """
    pattern = re.compile(r"(```[a-z]*\n[\s\S]*?\n```)|(`[^`\n]+`)")
    return pattern.sub('', markdown)

def remove_images_and_links(markdown):
    """
    Removes all images from a markdown string.
    markdown: a string of markdown
    """
    pattern = re.compile(r'\!\[.*\]\(.*\)')
    markdown = pattern.sub('', markdown)
    pattern = re.compile(r'\[.*\]\(.*\)')
    return pattern.sub('', markdown)


def remove_tables(markdown):
    """
    Removes all tables from a markdown string.
    markdown: a string of markdown
    """
    pattern = re.compile(r'\|.*\|')
    return pattern.sub('', markdown)

def remove_whitespace(markdown):
    """
    Removes all whitespace from a markdown string.
    markdown: a string of markdown
    """
    pattern = re.compile(r'\s+')
    return pattern.sub(' ', markdown)

def remove_hashes_and_pipe(markdown):
    """
    Removes all hashes and pipes from a markdown string.
    markdown: a string of markdown
    """
    markdown = re.sub(r'\|', '', markdown)
    markdown =re.sub(r'#+', '', markdown)
    return markdown

def alpha_numeric_only(text):
    """
    converts a string to alphanumeric only
    text: a string
    """
    return re.sub(r'\W+', '', text)




def generate_content_modules(file = here("data/modules.json"), text_only = False):
    """
    Generates content modules from a json file (HTML to markdown)
    file: a string of the json file path
    text_only: a boolean indicating whether to remove all non-text elements from the markdown
    """
    if text_only:
        folder_to_save = here("content_modules/content_only_text")
    else:
        folder_to_save = here("content_modules/content")

    if not os.path.exists(folder_to_save):
        os.makedirs(folder_to_save)        

    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        for i, module in enumerate(data):
            # get content
            content = module['content']
            markdown = md(content, heading_style="ATX", code_language = "javascript")
        
            if text_only:
                markdown = remove_code_blocks(markdown)
                markdown = remove_images_and_links(markdown)
                markdown = remove_tables(markdown)
                markdown = remove_whitespace(markdown)
                markdown = remove_hashes_and_pipe(markdown)
                markdown = markdown.strip()
            
            title = alpha_numeric_only(module["title"])
            with open(os.path.join(folder_to_save, f"{i}".zfill(3) + f"_{title}.md" ), "w", encoding="utf-8") as f:
                f.write(markdown)
    

if __name__ == "__main__":
    generate_content_modules( text_only = True )
 


