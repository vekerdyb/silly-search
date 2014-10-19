import sys
from Index import SimpleIndex

index = SimpleIndex('data.csv')

user_quits = False

while not user_quits:

    keyword = raw_input('Please enter keyword: ').decode(sys.stdin.encoding)

    if keyword == "":
        user_quits = True
        continue

    results = index.find_word(keyword)

    print 'Results for "%s":' % keyword

    for number, doc in enumerate(results):
        print ' %d)\t%s' % (number + 1, doc)

    print
