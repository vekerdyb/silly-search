from Index import Index

ind = Index('data.csv')

keyword = raw_input('Please enter keyword: ')

while keyword:
    print 'Results for "%s":' % keyword
    for number, doc in enumerate(ind.find_word(keyword)):
        print ' %d)\t%s' % (number + 1, doc)
    print
    keyword = raw_input('Please enter keyword: ')
