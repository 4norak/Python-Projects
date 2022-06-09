# Oneliner to open a file, read its content, close the file descriptor properly and return the content
lambda file: tuple(map(lambda x: x[0](x[1]), zip((lambda x: next(x).read(), lambda x: next(x).close(),), __import__("itertools").tee((open(file, "r"),), 2))))[0]
