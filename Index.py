import unicodecsv as csv
from bs4 import BeautifulSoup
from glob import glob


class Index():
    """
    Assumptions:
    We store the data as follows:
    - the data is in a comma separated file
    - the first value in a row is the document ID
    - from the second value on, the list of words from the document follow
    """

    def __init__(self, filename):
        self.filename = filename
        self.datafile = None

    def get_handler(self, method):
        """
        :param string method: the open() method. 'a' for append, 'w' for write, 'r' for read.
        :return: a csv reader / writer depending on the method
        """
        self.datafile = open(self.filename, method)
        if 'r' in method:
            return csv.reader(self.datafile)
        else:
            return csv.writer(self.datafile)

    def find_word(self, keyword):
        """
        Returns all documents' IDs that contain the keyword.

        :param string keyword: the search keyword
        :return: list of document IDs that contain the keyword
        """
        handler = self.get_handler('r')
        results = []
        for row in handler:
            for saved_word in row[1:]:
                if saved_word.lower() == keyword.lower():
                    results.append(row[0])
        self.datafile.close()
        return results

    def add_document(self, document_id, words):
        """
        Adds a document to the index

        :param string document_id:  the documents identifier (string)
        :param list words: list of words
        :return: None
        """
        handler = self.get_handler('a')
        handler.writerow([document_id] + words)
        self.datafile.close()

    def add_documents_from_folder(self, pattern):
        """
        Adds several documents matching the pattern.
        :param string pattern: glob pattern
        :return: None
        """
        for document in glob(pattern):
            html_file = open(document, 'r')
            text = BeautifulSoup(html_file.read()).get_text()
            words = [w.strip() for w in text.split(' ') if w.strip()]
            self.add_document(document, words)
            print 'Added "%s" to the index' % (document, )


    def delete(self):
        """
        Deletes the index file's contents
        :return: None
        """
        open(self.filename, 'w').close()


if __name__ == '__main__':
    ind = Index('data.csv')
    ind.delete()
    ind.add_documents_from_folder('htmls/*.html')
    for word in ['this', 'it', 'search']:
        print 'Results for "%s":' % word
        for number, doc in enumerate(ind.find_word(word)):
            print ' %d)\t%s' % (number + 1, doc)
        print


