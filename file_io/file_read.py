# # Method 1
# jabber = open("/Users/Sami/Downloads/sample.txt", 'r')
#
# for line in jabber:
#     print(line, end='')
#
# jabber.close()


# Method 2 - No need to close jabber, as the `with` statement takes care of that for us
#            `With` will also close the file, should Python encounter an error while reading the file
with open("/Users/Sami/Downloads/sample.txt") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')
