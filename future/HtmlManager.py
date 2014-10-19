from bs4 import BeautifulSoup


class HtmlHandler(object):
    def __init__(self, html):
        self.html = html
        self.text = BeautifulSoup(self.html).get_text()
        self.raw_words = [word.strip() for word in self.text.split(' ')
                          if word.strip()]

    def get_words_list(self):
        """
        :return: list of words occurring in the HTML's text
        """
        return self.raw_words

    def get_words_dict(self):
        """
        :return: dictionary of (word, count) pairs
        """
        words = {}
        for raw_word in self.raw_words:
            try:
                words[raw_word.lower()] += 1
            except KeyError:
                words[raw_word.lower()] = 1
        return words


if __name__ == "__main__":
    source = ('<a> This is a random text   the red fox jumps over the lazy '
              'dog </a></body>')
    h = HtmlHandler(source)
    for w in h.get_words_dict().items():
        print w
