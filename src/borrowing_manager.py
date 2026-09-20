borrowed_books = []


def borrow_book():
    book = input("Enter book to borrow: ")
    borrowed_books.append(book)
    print(f"{book} borrowed successfully!")


def return_book():
    book = input("Enter book to return: ")

    if book in borrowed_books:
        borrowed_books.remove(book)
        print(f"{book} returned successfully!")
    else:
        print("Book not found in borrowed list.")