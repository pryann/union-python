import books

while True:
    command = input("""Válaszd ki milyen műveletet szeretnél végrehajtani: 
1 - Könyvek listázása
2 - Könyv keresése
3 - Könyv felvétele
4 - Könyv módosítása
5 - Könyv törlése
6 - Kilépés                
""")
    if command == "1":
        books.list_books()
    elif command == "2":
        books.find_book()
    elif command == "3":
        books.create_book()
    elif command == "4":
        books.update_book()
    elif command == "5":
        books.delete_book()
    elif command == "6":
        break
    else:
        print("Nem létező parancs!")
