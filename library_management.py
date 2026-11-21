
books = {}

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "issued": False
    }

    print("Book added successfully!")

def view_books():
    if not books:
        print("No books available.")
        return

    for book_id, book in books.items():
        status = "Issued" if book["issued"] else "Available"

        print("\nBook ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", status)

def search_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found.")

def issue_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        if not books[book_id]["issued"]:
            books[book_id]["issued"] = True
            print("Book issued successfully!")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")

def return_book():
    book_id = input("Enter book ID: ")

    if book_id in books:
        if books[book_id]["issued"]:
            books[book_id]["issued"] = False
            print("Book returned successfully!")
        else:
            print("Book was not issued.")
    else:
        print("Book not found.")

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
