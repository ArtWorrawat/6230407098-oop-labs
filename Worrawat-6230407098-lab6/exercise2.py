form = (2, 123.4567, 10000, 12345.67)

if form[0] < 10:
    filename = "file_000" + str(form[0])
elif form[0] < 100:
    filename = "file_00" + str(form[0])
elif form[0] < 1000:
    filename = "file_0" + str(form[0])
elif form[0] < 10000:
    filename = "file_" + str(form[0])

print("{}: {:.2f}, {:.2e}, {:.2e}".format(filename, form[1], form[2], form[3]))


