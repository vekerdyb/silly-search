import unicodecsv as csv
from bs4 import BeautifulSoup
from glob import glob


class SimpleIndex(object):
    """
    Assumptions:
    We store the data as follows:
    - the data is in a comma separated file
    - the first value in a row is the document ID
    - from the second value on, the list of words from the document follow
    """

    def __init__(self, filename):
        """
        Initiates index from filename

        :param string filename: the index file (csv).
        :return: None
        """
        self.filename = filename
        self.datafile = None

    def _get_handler(self, method):
        """
        Returns a CSV file handler.

        :param string method: the open() method. 'a' for append, 'w' for write,
            'r' for read.
        :return: a csv reader / writer depending on the method
        """
        self.datafile = open(self.filename, method)
        if 'r' in method:
            return csv.reader(self.datafile)
        else:
            return csv.writer(self.datafile)

    def add_document(self, document_id, words):
        """
        Adds a document to the index

        :param string document_id:  the documents identifier (string)
        :param list words: list of words
        :return: None
        """
        handler = self._get_handler('a')
        handler.writerow([document_id] + words)
        self.datafile.close()
        print 'Added %r to the index with %d words' % (document_id, len(words))

    def _get_words_from_html(self, filename):
        html_file = open(filename, 'r')
        soup = BeautifulSoup(html_file.read())
        text_pieces = soup.find_all(['title', 'body'])
        text = ""
        for t in text_pieces:
            text += t.getText().replace('\n', ' ')

        words = [w.strip() for w in text.split(' ') if w.strip()]
        return words

    def add_documents_from_directory(self, pattern):
        """
        Adds several documents matching the pattern.

        :param string pattern: glob pattern
        :return: None
        """
        for document in glob(pattern):
            words = self._get_words_from_html(document)
            self.add_document(document, words)

    def find_word(self, keyword):
        """
        Returns all documents' IDs that contain the keyword.

        :param string keyword: the search keyword
        :return: list of document IDs that contain the keyword
        """
        keyword.encode('utf-8')
        database_handler = self._get_handler('r')
        results = []
        for row in database_handler:
            for saved_word in row[1:]:
                if saved_word.lower() == keyword.lower():
                    results.append(row[0])
        self.datafile.close()
        return results

    def delete(self):
        """
        Deletes the index file's contents
        :return: None
        """
        open(self.filename, 'w').close()
