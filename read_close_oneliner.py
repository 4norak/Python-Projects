# Oneliner to open a file, read its content, close the file descriptor properly and return the content
lambda file: tuple(map(lambda x: x[0](x[1]), zip((lambda x: x.read(), lambda x: x.close(),), (open(file, "r"),)*2)))[0]
