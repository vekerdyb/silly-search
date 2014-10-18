import unicodecsv as csv
from unicode_helper import remove_non_letters


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
        words = [remove_non_letters(w) for w in words]
        handler.writerow([document_id] + words)
        self.datafile.close()

    def delete(self):
        """
        Deletes the index file's contents
        :return: None
        """
        open(self.filename, 'w').close()


if __name__ == '__main__':
    ind = Index('data.csv')
    ind.delete()
    ind.add_document('first.html', u'this is the best search engine i could come up with in 20 minutes'.split(' '))
    ind.add_document('second.html',
                     u'however it is not a very sophisticated search engine and it is potentially very slow'.split(' '))

    ind.add_document('third.html',
                     u'BUT IT CAN SEARCH FOR UPPERCASE WORDS AS WELL, ISN\'T THAT JUST AWESOME?'.split(' '))

    for word in ['this', 'it', 'search']:
        print 'Results for "%s":' % word
        for number, doc in enumerate(ind.find_word(word)):
            print ' %d)\t%s' % (number + 1, doc)
        print


