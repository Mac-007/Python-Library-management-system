# This is a deliberately poorly implemented main script for a Library Management System.

#import book_management
#import user_management
#import checkout_management

import os
import pandas as pd

from user import User_details
from book import book_management
from storage import storage_management
from check import check_out

user_details_csv = './User_details.csv'
books_record_details_csv = './books_record_details.csv'

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Exit")
    choice = input("Enter choice: ")
    return choice


def main():
    store_obj=storage_management(user_details_csv,books_record_details_csv)
    store_obj.check_user_details()
    store_obj.check_book_details()
    
    while True:
        choice = main_menu()
        if choice == '1':           # Add books
            title = input("Enter title: ")
            while not title.strip():  # Check if the title is empty or blank
                print("title cannot be empty or blank.")
                title = input("Enter title: ")
                
            author = input("Enter author: ")
            while not author.strip() or any(char.isdigit() for char in author.strip()) or not author.strip().isalpha():
                if not author.strip(): # Check if the author is empty or blank
                    print("Author cannot be empty or blank.")
                elif any(char.isdigit() for char in author.strip()):     # Check if the author contains digits
                    print("Author cannot contain digits.")
                elif not author.strip().isalpha():  # Check if the author contains non-alphabetic characters
                    print("Author must contain only alphabetic characters.")
                author = input("Enter author: ")
                
            isbn = input("Enter ISBN: ")
            while not isbn.strip() or not isbn.isdigit():  # Check if the ID is empty or blank or not a number
                if not isbn.strip():                         # Check if the ID is empty or blank
                    print("ISBN cannot be empty or blank.")
                elif not isbn.isdigit():                     # Check if the ID is number or not
                    print("ISBN must contain only numbers.")
                isbn = input("Enter ISBN: ")
            
            book = book_management(books_record_details_csv)
            book.add_book(title, author, isbn)
            print("Book added.")
            
        elif choice == '2':     # List Books
            book2 = book_management(books_record_details_csv)
            book2.list_books()
            
        elif choice == '3':     # Add User
            name = input("Enter user name: ")
            while not name.strip():  # Check if the input is empty or blank
                print("Name cannot be empty or blank.")
                name = input("Enter user name: ")
            
            user_id = input("Enter user ID: ")
            while not user_id.strip() or not user_id.isdigit():  # Check if the ID is empty or blank or not a number
                if not user_id.strip():                         # Check if the ID is empty or blank
                    print("User ID cannot be empty or blank.")
                elif not user_id.isdigit():                     # Check if the ID is number or not
                    print("User ID must contain only numbers.")
                user_id = input("Enter user ID: ")
            
            user=User_details(name,user_id,user_details_csv)
            user.add_user()
            
        elif choice == '4':     # Checkout Book
            user_id = input("Enter user ID: ")
            while not user_id.strip() or not user_id.isdigit():  # Check if the ID is empty or blank or not a number
                if not user_id.strip():                         # Check if the ID is empty or blank
                    print("User ID cannot be empty or blank.")
                elif not user_id.isdigit():                     # Check if the ID is number or not
                    print("User ID must contain only numbers.")
                user_id = input("Enter user ID: ")
                    
            isbn = input("Enter ISBN: ")
            while not isbn.strip() or not isbn.isdigit():  # Check if the ID is empty or blank or not a number
                if not isbn.strip():                         # Check if the ID is empty or blank
                    print("ISBN cannot be empty or blank.")
                elif not isbn.isdigit():                     # Check if the ID is number or not
                    print("ISBN must contain only numbers.")
                isbn = input("Enter ISBN: ")
                    
            checkout_obj=check_out(user_id,isbn,user_details_csv,books_record_details_csv)

            checkout_obj.checkout_book()
            #print("Book checked out.")
            
        elif choice == '5':     #Exit
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()