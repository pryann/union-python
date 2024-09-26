from os import chdir, path

chdir(path.join(path.dirname(__file__), "files"))

with open("text.txt", "r") as file:
    pass
    # print(file.read())
    # file.seek(0)
    # print(file.read())
    # print(file.readlines())
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # for line in file:
    #     for char in line:
    # print(char)

# with open(file="text2.txt", mode="w", encoding="UTF-8") as file:
#     content = ["Hello", "World", "Python"]
#     for i in content:
#         file.write(i + "\n")

with open(file="text2.txt", mode="a", encoding="UTF-8") as file:
    content = ["PHP", "Ruhy", "JS"]
    for i in content:
        file.write(i + "\n")
