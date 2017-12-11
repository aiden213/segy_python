#import codecs

with open("test.sgy", "rt", encoding="cp037") as ebcdic:
    i = 0
    while i < 40:
        print(ebcdic.read(80))
        i = i + 1


  # print(ebcdic.read(80))
#   print ('\n')
# with open("123.txt", "r") as test:
#     print (test.readline())
