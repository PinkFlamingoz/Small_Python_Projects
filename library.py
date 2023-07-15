# Import
import csv
import errno
import os
import sys
from basic_functions import get_valid_input


# Classes
class Library():
    
    # Constructor
    def __init__(self, filename):
        self.filename = filename
        self.books = [] #------------------------------------------------------------------ Initialize books as an empty list
            
        # Check if directory exists, if not create it
        dir_name = os.path.dirname(filename)
        if dir_name: #--------------------------------------------------------------------- If directory is not an empty string
            if not os.path.exists(dir_name):
                try:
                    os.makedirs(dir_name)
                except OSError as e: #----------------------------------------------------- Guard against race condition
                    if e.errno != errno.EEXIST:
                        raise
                    else:
                        print(f"\nFailed to create directory: {os.path.dirname(filename)}")
                        print(f"\nOS error: {e}")

        # Load books from file if it exists
        if os.path.isfile(filename):
            self.load_from_csv()


    # Method to load books from a CSV file
    def load_from_csv(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert 'read' field from string to boolean
                    read_status = False if row["read"].lower() == 'false' else True
                    self.books.append({"title": row["title"], "author": row["author"], "read": read_status})
        except OSError as e:
            print(f"\nFailed to open file: {self.filename}")
            print(f"\nOS error: {e}")


    # Method to write books to a CSV file
    def write_to_csv(self):
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["title", "author", "read"])
                writer.writeheader()
                writer.writerows(self.books)
        except OSError as e:
            print(f"\nFailed to open file: {self.filename}")
            print(f"\nOS error: {e}")


    # Method to add a book
    def add_book(self, title, author, read = False):
        self.books.append({"title": title, "author": author, "read": read})
        # Write the updated books list to the file
        self.write_to_csv()
        print(f"\n\tBook '{title}' added.")


    # Method to delete a book
    def delete_book(self, title):
        self.books = [book for book in self.books if book["title"].lower() != title.lower()]
        # Write the updated books list to the file
        self.write_to_csv()
        print(f"\n\tBook '{title}' deleted.")


    # Method to search for a book
    def search_book(self, title):
        return [book for book in self.books if book["title"].lower() == title.lower()]


    # Method to mark a book as read
    def mark_book(self, title):
        # Find the book in the list of books
        for book in self.books:
            if book["title"].lower() == title.lower():
                
                # Mark the book as read
                answer = get_valid_input(str, "Do you want to mark this book as read? \nPress enter for False, Enter anything for True ")
                if answer:
                    book["read"] = True
                    print(f"\nBook '{title}' marked as read.")
                else:
                    book["read"] = False
                    print(f"\nBook '{title}' marked as unread.")
                
                # Write the updated books list to the file
                self.write_to_csv()
                return
       
        # If the book wasn't found in the list
        print(f"\nNo book with title '{title}' found.")

    
    # Method to display all books
    def display_all_books(self):
        return self.books


    # Method to display all authors
    def display_all_authors(self):
        return [book["author"] for book in self.books]


    # Method to display all read books
    def display_read_books(self):
        return [book for book in self.books if book["read"]]


    # Method to display all unread books
    def display_unread_books(self):
        return [book for book in self.books if not book["read"]]


    # Method to display the whole library
    def display_library(self):
        for book in self.books:
            print('Title: {:50} Author: {:30} Read: {}'.format(book['title'], book['author'], book['read']))
    
            
    # Method to delete all books
    def delete_all_books(self):
        # Clear the list
        self.books = []

        # Open the file in write mode, which will erase its contents
        try:
            with open(self.filename, "w") as file:
                writer = csv.DictWriter(file, fieldnames=["title", "author", "read"])
                writer.writeheader()
        except OSError as e:
            print(f"\nFailed to open file: {self.filename}")
            print(f"\nOS error: {e}")

        print("\nAll books have been deleted from the library.")
    

# Main
def main():
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
    if len(sys.argv) != 1 and len(sys.argv) != 2:
       
        print("\nError 1: Too many or none arguments  \n Usage: python library.py [library.cvs]\n")
        sys.exit(1)
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
    
    # Determine cvs file to use
    file_name = sys.argv[1] if len(sys.argv) == 2 else "DATA/library.csv"
    lib = Library(file_name)

    while True:
        print_menu()
        case = get_valid_input(int, "\n\tEnter choice: ")
        if case == 1:
            print("\nJust press enter for read if book is not completed!")
            lib.add_book(get_valid_input(str,"Enter title: "), get_valid_input(str,"Enter author: "), get_valid_input(bool,"Enter read: "))
        elif case == 2:
            lib.delete_book(get_valid_input(str,"\n\tEnter title: "))
        elif case == 3:
            book = lib.search_book(get_valid_input(str,"\n\tEnter title: "))
            print(book)
        elif case == 4:
            lib.mark_book(get_valid_input(str,"\n\tEnter title: "))
        elif case == 5:
            books = lib.display_all_books()
            for book in books:
                print('Title: {:50} Author: {:30} Read: {}'.format(book['title'], book['author'], book['read']))
        elif case == 6:
            authors = lib.display_all_authors()
            for author in authors:
                print(f"Author: {author}")
        elif case == 7:
            books = lib.display_read_books()
            for book in books:
                print('Title: {:50} Author: {:30} Read: {}'.format(book['title'], book['author'], book['read']))
        elif case == 8:
            books = lib.display_unread_books()
            for book in books:
                print('Title: {:50} Author: {:30} Read: {}'.format(book['title'], book['author'], book['read']))
        elif case == 9:
            lib.display_library()
        elif case == 10:
            lib.delete_all_books() 
        elif case == 11:
            os.system("cls" if os.name == "nt" else "clear")
        elif case == 0:
            break
        input("\n\t\tPress Enter to continue...")


# Print the menu
def print_menu():
    options = [
        "Add a book",
        "Delete a book",
        "Search for a book",
        "Mark a book",
        "Display all books",
        "Display all authors",
        "Display all read books",
        "Display all unread books",
        "Display the whole library",
        "Delete all books",
        "Clear screen"
    ]

    print("\nWhat operation do you want to perform? Select Option number. Enter 0 to exit.\n")
    for i, option in enumerate(options, start = 1):
        print(f"\t{i}. {option}")
        

# Start
if __name__ == "__main__":    
    main()