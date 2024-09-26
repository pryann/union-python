from os import path, getcwd

print("getcwd: ", getcwd())
print("__file__: ", __file__)
print("dirname: ", path.dirname(__file__))
print("basename: ", path.basename(__file__))

# working dir + files + filename
# print(path.join(getcwd(), "03_day", "files", "text.txt"))
print(path.join(path.dirname(__file__), "files", "text.txt"))
