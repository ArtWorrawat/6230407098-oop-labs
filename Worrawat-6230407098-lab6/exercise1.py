ftuple = (2, 10, 11, 3, 1000)
filename = []
for i in ftuple:
    if i < 10:
        fileadd = "file_000" + str(i)
    elif i < 100:
        fileadd = "file_00" + str(i)
    elif i < 1000:
        fileadd = "file_0" + str(i)
    elif i < 10000:
        fileadd = "file_" + str(i)
    filename.append(fileadd)

print("{:30}{}".format("input filenames are", ftuple))
print("{:30}{}".format("zero padded filenames", filename))
filename.sort()
print("{:30}{}".format("sorted filename are", filename))