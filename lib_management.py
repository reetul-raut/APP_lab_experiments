class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" added successfully.')

    def view_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You borrowed "{book}".')
        else:
            print("Book not available.")

    def return_book(self, book):
        self.books.append(book)
        print(f'You returned "{book}".')


def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book = input("Enter book name: ")
            library.add_book(book)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book = input("Enter book name to borrow: ")
            library.borrow_book(book)

        elif choice == "4":
            book = input("Enter book name to return: ")
            library.return_book(book)

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()