import json

# Library ko store karne ke liye ek list
library = []

# Function to add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"
    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
    library.append(book)
    print("Book added successfully!")

# Function to remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library[:]:  # Copy of library to avoid iteration issues
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")

# Function to search for a book
def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        matches = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        matches = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice!")
        return
    
    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matches found!")

# Function to display all books
def display_books():
    if not library:
        print("Your library is empty!")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Function to display statistics
def display_stats():
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty!")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage:.1f}%")

# Function to save library to a file
def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)
    print("Library saved to file.")

# Function to load library from a file
def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)
    except FileNotFoundError:
        library = []  # If file doesn't exist, start with empty library

# Main menu
def main():
    load_library()  # Program start hone par library load karo
    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()