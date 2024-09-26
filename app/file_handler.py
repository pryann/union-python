def read_file(file_path):
    books = []
    with open(file_path, "r") as file:
        for line in file:
            id, author, title = line.strip().split(";")
            books.append(
                {
                    "id": int(id),
                    "author": author,
                    "title": title,
                }
            )
    return books


def write_file(file_path, books):
    with open(file_path, "w") as file:
        for book in books:
            book_line = ";".join(str(val) for val in book.values())
            # TODO: remove the last character
            file.write(book_line + "\n")
