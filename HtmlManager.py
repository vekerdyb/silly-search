import requests
import re

links_regular_expression = re.compile("(http[s]?://[^\s\"><]+)")

def download(url):
    try:
        response = requests.get(url)
    except:
        return ""
    return response.text


def get_links(text):
    return links_regular_expression.findall(text)