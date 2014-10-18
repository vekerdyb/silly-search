from glob import glob

from Index import Index
from HtmlManager import HtmlHandler


index = Index('data.csv')
index.delete()

for doc in glob('htmls/*.html'):
    html_file = open(doc, 'r')
    html_handler = HtmlHandler(html_file.read())
    print doc
    index.add_document(doc, html_handler.get_words_list())
