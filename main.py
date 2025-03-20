


























import streamlit as st
import json
import os

# File path for storing book data
BOOKS_FILE = "books_data.json"

# Function to load books from JSON file
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Function to save books to JSON file
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Load books initially
books = load_books()

# Streamlit UI
st.title("📚 Personal Library Manager")

# Sidebar options
menu = st.sidebar.radio("Select an option:", ["Add Book", "View Books", "Update Book", "Delete Book", "Reading Progress"])

# Add a new book
if menu == "Add Book":
    st.header("➕ Add a New Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.text_input("Publication Year")
    genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science", "Technology", "Fantasy", "Romance", "History", "Other"])
    read_status = st.radio("Have you read this book?", ["Read", "Unread"])

    if st.button("Add Book"):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status == "Read"
        }
        books.append(new_book)
        save_books(books)
        st.success(f"✅ Book '{title}' added successfully!")
        st.experimental_rerun()

# View all books
elif menu == "View Books":
    st.header("📖 Your Book Collection")

    if books:
        for book in books:
            st.write(f"📚 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '📖 Unread'}")
    else:
        st.warning("No books found. Please add a book.")

# Update book details
elif menu == "Update Book":
    st.header("✏️ Update Book Details")

    book_titles = [book["title"] for book in books]
    if book_titles:
        selected_book = st.selectbox("Select a book to update", book_titles)
        for book in books:
            if book["title"] == selected_book:
                new_title = st.text_input("New Title", book["title"])
                new_author = st.text_input("New Author", book["author"])
                new_year = st.text_input("New Publication Year", book["year"])
                new_genre = st.text_input("New Genre", book["genre"])
                new_read_status = st.radio("Reading Status", ["Read", "Unread"], index=0 if book["read"] else 1)

                if st.button("Update Book"):
                    book["title"] = new_title
                    book["author"] = new_author
                    book["year"] = new_year
                    book["genre"] = new_genre
                    book["read"] = new_read_status == "Read"
                    save_books(books)
                    st.success("✅ Book updated successfully!")
                    st.experimental_rerun()
    else:
        st.warning("No books available to update.")

# Delete a book
elif menu == "Delete Book":
    st.header("🗑️ Remove a Book")

    book_titles = [book["title"] for book in books]
    if book_titles:
        selected_book = st.selectbox("Select a book to delete", book_titles)

        if st.button("Delete Book"):
            books = [book for book in books if book["title"] != selected_book]
            save_books(books)
            st.success(f"🗑️ Book '{selected_book}' deleted successfully!")
            st.experimental_rerun()
    else:
        st.warning("No books available to delete.")

# Show reading progress
elif menu == "Reading Progress":
    st.header("📊 Reading Progress")

    total_books = len(books)
    read_books = sum(1 for book in books if book["read"])
    completion_rate = (read_books / total_books * 100) if total_books > 0 else 0

    st.write(f"📚 Total Books: **{total_books}**")
    st.write(f"✅ Books Read: **{read_books}**")
    st.write(f"📊 Completion Rate: **{completion_rate:.2f}%**")# import json


# class BookCollection:
#     """A class to manage a collection of books, allowing users to store and organize their reading materials."""

#     def __init__(self):
#         """Initialize a new book collection with an empty list and set up file storage."""
#         self.book_list = []
#         self.storage_file = "books_data.json"
#         self.read_from_file()

#     def read_from_file(self):
#         """Load saved books from a JSON file into memory.
#         If the file doesn't exist or is corrupted, start with an empty collection."""
#         try:
#             with open(self.storage_file, "r") as file:
#                 self.book_list = json.load(file)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.book_list = []

    # def save_to_file(self):
    #     """Store the current book collection to a JSON file for permanent storage."""
    #     with open(self.storage_file, "w") as file:
    #         json.dump(self.book_list, file, indent=4)

    # def create_new_book(self):
    #     """Add a new book to the collection by gathering information from the user."""
    #     book_title = input("Enter book title: ")
    #     book_author = input("Enter author: ")
    #     publication_year = input("Enter publication year: ")
    #     book_genre = input("Enter genre: ")
    #     is_book_read = (
    #         input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    #     )

    #     new_book = {
    #         "title": book_title,
    #         "author": book_author,
    #         "year": publication_year,
    #         "genre": book_genre,
    #         "read": is_book_read,
    #     }

    #     self.book_list.append(new_book)
    #     self.save_to_file()
    #     print("Book added successfully!\n")

    # def delete_book(self):
    #     """Remove a book from the collection using its title."""
    #     book_title = input("Enter the title of the book to remove: ")

    #     for book in self.book_list:
    #         if book["title"].lower() == book_title.lower():
    #             self.book_list.remove(book)
    #             self.save_to_file()
    #             print("Book removed successfully!\n")
    #             return
    #     print("Book not found!\n")

    # def find_book(self):
    #     """Search for books in the collection by title or author name."""
    #     search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    #     search_text = input("Enter search term: ").lower()
    #     found_books = [
    #         book
    #         for book in self.book_list
    #         if search_text in book["title"].lower()
    #         or search_text in book["author"].lower()
    #     ]

    #     if found_books:
    #         print("Matching Books:")
    #         for index, book in enumerate(found_books, 1):
    #             reading_status = "Read" if book["read"] else "Unread"
    #             print(
    #                 f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
    #             )
    #     else:
    #         print("No matching books found.\n")

    # def update_book(self):
    #     """Modify the details of an existing book in the collection."""
    #     book_title = input("Enter the title of the book you want to edit: ")
    #     for book in self.book_list:
    #         if book["title"].lower() == book_title.lower():
    #             print("Leave blank to keep existing value.")
    #             book["title"] = input(f"New title ({book['title']}): ") or book["title"]
    #             book["author"] = (
    #                 input(f"New author ({book['author']}): ") or book["author"]
    #             )
    #             book["year"] = input(f"New year ({book['year']}): ") or book["year"]
    #             book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
    #             book["read"] = (
    #                 input("Have you read this book? (yes/no): ").strip().lower()
    #                 == "yes"
    #             )
    #             self.save_to_file()
    #             print("Book updated successfully!\n")
    #             return
    #     print("Book not found!\n")

    # def show_all_books(self):
    #     """Display all books in the collection with their details."""
    #     if not self.book_list:
    #         print("Your collection is empty.\n")
    #         return

    #     print("Your Book Collection:")
    #     for index, book in enumerate(self.book_list, 1):
    #         reading_status = "Read" if book["read"] else "Unread"
    #         print(
    #             f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
    #         )
    #     print()

    # def show_reading_progress(self):
    #     """Calculate and display statistics about your reading progress."""
    #     total_books = len(self.book_list)
    #     completed_books = sum(1 for book in self.book_list if book["read"])
    #     completion_rate = (
    #         (completed_books / total_books * 100) if total_books > 0 else 0
    #     )
    #     print(f"Total books in collection: {total_books}")
    #     print(f"Reading progress: {completion_rate:.2f}%\n")

    # def start_application(self):
        # """Run the main application loop with a user-friendly menu interface."""
        # while True:
        #     print("📚 Welcome to Your Book Collection Manager! 📚")
        #     print("1. Add a new book")
        #     print("2. Remove a book")
        #     print("3. Search for books")
        #     print("4. Update book details")
        #     print("5. View all books")
        #     print("6. View reading progress")
        #     print("7. Exit")
        #     user_choice = input("Please choose an option (1-7): ")

        #     if user_choice == "1":
        #         self.create_new_book()
        #     elif user_choice == "2":
        #         self.delete_book()
        #     elif user_choice == "3":
        #         self.find_book()
        #     elif user_choice == "4":
        #         self.update_book()
        #     elif user_choice == "5":
#                 self.show_all_books()
#             elif user_choice == "6":
#                 self.show_reading_progress()
#             elif user_choice == "7":
#                 self.save_to_file()
#                 print("Thank you for using Book Collection Manager. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.\n")


# if __name__ == "__main__":
#     book_manager = BookCollection()
#     book_manager.start_application()
