filename = input("Enter a filename:")
with open("{}.txt".format(filename), encoding="utf8") as thisfile:
    read = thisfile.read()
    print(read)
    thisfile.close()
