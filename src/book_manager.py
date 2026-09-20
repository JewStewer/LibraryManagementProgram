def add_book():
    book = input("Enter book name: ")
    with open("data/books.txt", "a") as file:
        file.write(book + "\n")
    print("Book added successfully!")


def view_books():
    print("\n--- Book List ---")
    try:
        with open("data/books.txt", "r") as file:
            books = file.readlines()
            for book in books:
                print(book.strip())
    except FileNotFoundError:
        print("No books found.")


def search_book():
    search = input("Enter book name to search: ")
    found = False

    with open("data/books.txt", "r") as file:
        books = file.readlines()

    for book in books:
        if search.lower() in book.lower():
            print("Found:", book.strip())
            found = True

    if not found:
        print("Book not found.")