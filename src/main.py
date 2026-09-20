from book_manager import add_book, view_books, search_book
from borrowing_manager import borrow_book, return_book
from report_manager import generate_report

def menu():
    while True:
        print ("\n= BrightPage Library System =")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            generate_report()
        elif choice == "7":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()