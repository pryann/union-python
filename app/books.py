from os import path

import crud
import file_handler

PATH = path.join(path.dirname(__file__), "books.csv")
books = file_handler.read_file(PATH)


def list_books():
    print(books)


def find_book():
    # TODO: check if id isdigit
    book_id = int(input("Add meg a keresendő könyv ID-ját: "))
    print(crud.find_item(book_id, books))


def create_book():
    keys = list(books[0].keys())
    keys.remove("id")
    book = {}
    for key in keys:
        data = input(f"Add meg az új könyv {key} értékét: ")
        if data:
            book[key] = data
    crud.create_item(book, books)
    file_handler.write_file(PATH, books)


def update_book():
    book_id = int(input("Add meg a módosítandó könyv ID-ját: "))
    book = crud.find_item(book_id, books)
    if book is None:
        print("Nem létező könyv!")
        return
    # separate to a new function and use it inside create and update functions
    keys = list(book.keys())
    keys.remove("id")
    for key in keys:
        data = input(f"Add meg a könyv új {key} értékét: ")
        if data:
            book[key] = data
    # author = input("Add meg a szerzőjének a nevét: ")
    # title = input("Add meg a könyv címét: ")
    # book.update({"author": author, "title": title})
    crud.update_item(book_id, book, books)
    file_handler.write_file(PATH, books)
    print("Könyv sikeresen módosítva!")


def delete_book():
    book_id = int(input("Add meg a törlendő könyv ID-ját: "))
    crud.delete_item(book_id, books)
    file_handler.write_file(PATH, books)
    print("Könyv sikeresen törölve!")
