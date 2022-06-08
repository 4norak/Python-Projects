# Oneliner to open a file, read its content, close the file descriptor properly and return the content
lambda file: tuple(map(lambda z: z[0](z[1]), zip((lambda x: x.__next__().read(), lambda y: y.__next__().close(),), __import__("itertools").tee((open(file, "r"),), 2))))[0]
