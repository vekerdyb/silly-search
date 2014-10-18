def remove_non_letters(word):
    return word.translate(word_unicode_remove)



class NonLetterRemoval(dict):

    def __missing__(self, item):
        uni = unichr(item)
        res = u""
        if uni.isupper() or uni.islower():
            res = uni
        self[item] = res
        return res

word_unicode_remove = NonLetterRemoval()
