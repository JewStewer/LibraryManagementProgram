from book_manager import view_books
from borrowing_manager import borrowed_books


def generate_report():
    print("\n===== Library Report =====")

    print("\nAvailable Books:")
    view_books()

    print("\nBorrowed Books:")
    if borrowed_books:
        for book in borrowed_books:
            print(book)
    else:
        print("No borrowed books.")