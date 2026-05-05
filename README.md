# Library Management System

A Python-based library management system that simulates a real library with support for multiple item types, user management, borrowing/returning items, and overdue fine calculation.

## Features

- **Multiple Item Types**: Books, DVDs, and Magazines with different borrowing rules
- **User Management**: Support for Students (borrowers) and Librarians (administrators)
- **Borrowing System**: Borrow and return items with availability tracking
- **Borrowing Limits**: Per-category limits to prevent hoarding
- **Fine Calculation**: Automatic overdue fine calculation based on item type
- **Interactive CLI**: Menu-driven interface for library operations

## Item Types & Rules

| Item Type | Loan Duration | Borrowing Limit | Fine per Day |
|-----------|---------------|-----------------|--------------|
| Book      | 21 days       | 3 items         | £0.25        |
| Magazine  | 14 days       | 5 items         | £0.20        |
| DVD       | 7 days        | 2 items         | £0.50        |

## Installation

```bash
git clone https://github.com/KasGreen/Library.git
cd Library
```

## Usage

Run the library system:

```bash
python library.py
```

You will be prompted to enter a librarian ID. Use the default librarian ID `7248` to access the system.

### Available Operations

1. Display all books
2. Display all magazines
3. Display all DVDs
4. Display all students
5. Display all librarians
6. Borrow an item
7. Return an item
8. Add a new book
9. Add a new magazine
10. Add a new DVD
11. Register a new student
12. Register a new librarian
13. Move day forward (simulates time passing)
14. Move 10 days forward

## Class Structure

### Items

```
Item (base class)
├── Book
├── DVD
└── Magazine
```

### Users

```
User (base class)
├── Student (can borrow items)
└── Librarian (manages library)
```

### Library

The `Library` class manages collections of items and users, providing methods for:
- Adding/finding items by type and identifier
- Registering/finding users by type and ID
- Processing borrow and return transactions
- Displaying available items and registered users

## API Reference

### Item Class

```python
Item(title, author, identifier, available, limit, duration, fine)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | str | Item title |
| `author` | str | Author/creator name |
| `identifier` | int | Unique identifier (ISBN for books) |
| `available` | bool | Availability status |
| `limit` | int | Max items a user can borrow of this type |
| `duration` | int | Loan period in days |
| `fine` | float | Fine per day when overdue |

### User Class

```python
User(name, user_id, borrowed_items)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | str | User's name |
| `user_id` | int | Unique user identifier |
| `borrowed_items` | list | List of currently borrowed items |

### Library Class

```python
Library(items, users)
```

**Key Methods:**

| Method | Description |
|--------|-------------|
| `add_item(item)` | Add any item to the library |
| `add_book(item)` | Add a book (with duplicate check) |
| `add_magazine(item)` | Add a magazine (with duplicate check) |
| `add_dvd(item)` | Add a DVD (with duplicate check) |
| `register_student(user)` | Register a new student |
| `register_librarian(user)` | Register a new librarian |
| `borrow_item(student_id, identifier)` | Process item borrowing |
| `return_item(student_id, identifier)` | Process item return |
| `find_item(identifier)` | Find item by identifier |
| `find_student(user_id)` | Find student by ID |
| `display_all_available_items()` | Show all available items |

## Example

```python
from library import Book, Magazine, Student, Library

# Create items
book = Book('1984', 'George Orwell', 123456, True)
magazine = Magazine('National Geographic', 'NatGeo', 789, True)

# Create users
student = Student('Alice', 1001, [])

# Create library and populate
library = Library([], [])
library.add_book(book)
library.add_magazine(magazine)
library.register_student(student)

# Borrow an item
library.borrow_item(1001, 123456)  # Alice borrows 1984

# Return an item
library.return_item(1001, 123456)  # Alice returns 1984
```

## Pre-loaded Data

The system comes with sample data:

**Books:**
- Harry Potter (J.K. Rowling)
- Barry Hopper (R.N. Howling)
- book3, book4

**Magazines:** mag1, mag2

**DVDs:** DVD1, DVD2

**Users:**
- Librarian: Kas (ID: 7248)
- Students: Steve (ID: 6734), Larry (ID: 5435)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

KasGreen

---

*Note: This is an educational project demonstrating object-oriented programming concepts in Python including inheritance, encapsulation, and polymorphism.*
