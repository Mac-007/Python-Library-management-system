# Library Management System

Welcome to the **Library Management System**! This project is designed to streamline the process of managing a library, including functionalities such as user account generation, book searches, and book issuing. The system leverages Python's Object-Oriented Programming (OOP) concepts, file handling, and the Pandas library to ensure efficient data management and validation.

## Features

- **User Account Generation**: Create and manage user accounts, allowing users to borrow and return books.
- **Admin User Management**: Admin can check user details and manage user accounts.
- **Book Availability Check**: Verify the availability of books in the library.
- **Book Search**: Search for books by title, ID, or author name.
- **Book Issuing**: Issue books to users and manage book return.
- **Input Validation**: Ensure all user inputs are in the required format and validate entries to maintain data integrity.

## Project Structure

The project consists of several Python files, each serving a specific purpose:

- **User_details.csv**: Stores user account information.
- **book.py**: Contains the `Book` class and related methods.
- **books_record_details.csv**: Stores information about the books in the library.
- **check.py**: Includes functions for input validation and checking book/user details.
- **main.py**: The main entry point of the application, coordinating various functionalities.
- **models.py**: Defines the data models used throughout the application.
- **storage.py**: Handles file operations and data storage.
- **user.py**: Contains the `User` class and related methods.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. Install the required dependencies:
    ```bash
    pip install pandas
    ```

### Usage

Run the main script to start the application:
```bash
python main.py
```

Follow the on-screen instructions to navigate through the various features of the Library Management System.

## Code Overview

### `book.py`

Defines the `Book` class, encapsulating attributes like `title`, `author`, `id`, and methods to interact with book objects.

### `user.py`

Defines the `User` class, managing user-specific data and methods to manipulate user information.

### `models.py`

Contains the data models used for the library management system, including user and book data structures.

### `storage.py`

Handles all file operations, including reading from and writing to CSV files.

### `check.py`

Includes utility functions for validating inputs and checking the existence and details of books and users.

### `main.py`

Acts as the entry point for the application, providing a user interface and orchestrating interactions between different modules.

## License

This project is licensed under an open license. You are free to use, modify, and distribute this software as needed. 

There are no restrictions on how the software can be used. I hope this project is beneficial to you and look forward to any contributions you may make.

## Acknowledgements

Thank you for using the Library Management System. We hope it helps make managing your library a breeze!

---

Feel free to reach out with any questions or feedback (amitchougule121@gmail.com). Happy coding!
