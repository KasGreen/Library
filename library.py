class Book:
	def __init__(self, title, author, isbn, available):
		self.title = title
		self.author = author
		self.isbn = isbn
		self.available = available

	def display_book_info(self):
		print('Title: ' + self.title + '\nAuthor: ' + self.author + '\nisbn: ' + str(self.isbn))
		if self.available == True:
			print('This book is currently available\n\n')
		else:
			print('This book is currently unavailable\n\n')

	def __str__(self):
		return self.title

class User:
	def __init__(self, name, user_id, borrowed_books):
		self.name = name
		self.user_id = user_id
		self.borrowed_books = borrowed_books

	def borrow_book(self, book):
		if book.available == False:
			return 'unavailable'
		if len(self.borrowed_books) >= 3:
			return 'limit reached'
		self.borrowed_books.append(book)
		book.available = False
		return 'available'

	def return_book(self, book):
		if book.available == True or book not in self.borrowed_books:
			return False
		self.borrowed_books.remove(book)
		book.available = True
		return True

	def display_user_info(self):
		print('Name: ' + self.name + '\nUser id: ' + str(self.user_id) + '\nBorrowed books:\n')
		for i in range(0, len(self.borrowed_books)):
			print(self.borrowed_books[i])


class Library:
	def __init__(self, books, users):
		self.books = books
		self.users = users

	def add_book(self, book):
		if self.find_book(book.isbn) != None:
			print(book.title + ' is already registered in the library') 
		else:
			self.books.append(book)

	def register_user(self, user):
		if self.find_user(user.user_id) != None:
			print('The id ' + str(user.user_id) + ' is already registered to another user in the library')
		else:
			self.users.append(user)

	def find_book(self, isbn):
		for i in range(0, len(self.books)):
			book = self.books[i]
			if book.isbn == isbn:
				return book
		return None

	def find_user(self, user_id):
		for i in range(0, len(self.users)):
				user = self.users[i]
				if user.user_id == user_id:
					return user
		return None

	def borrow_book(self, user_id, isbn):
		book_to_borrow = self.find_book(isbn)
		if book_to_borrow == None:
			print(str(isbn) + ' is not a registered book in the library')
			return
		user = self.find_user(user_id)
		if user == None:
			print(str(user_id) + ' is not a registered user id')
			return
		result = user.borrow_book(book_to_borrow)
		if result == 'available':
			print(user.name + ' has borrowed ' + book_to_borrow.title)
		if result == 'unavailable':
			print(book_to_borrow.title + ' is currently unavailable')
		if result == 'limit reached':
			print(book_to_borrow.title + ' could not be borrowed since ' + user.name + ' has already borrowed 3 books')

	def return_book(self, user_id, isbn):
		book_to_return = self.find_book(isbn)
		if book_to_return == None:
			print(str(isbn) + ' is not a registered book in the library')
			return
		user = self.find_user(user_id)
		if user == None:
			print(str(user_id) + ' is not a registered user id')
			return
		result = user.return_book(book_to_return)
		if result == True:
			print(user.name + ' has returned ' + book_to_return.title)
		if result == False:
			print(book_to_return.title + ' cannot be returned')				

	def display_all_books(self):
		print('Books:\n')
		for i in range(0, len(self.books)):
			print(self.books[i])


	def display_all_users(self):
		print('Users:\n')
		for i in range(0, len(self.users)):
			print(self.users[i].name)

b1 = Book('Harry Potter', 'J. K. Rowling', 2131231, True)
b2 = Book('Barry Hopper', 'R. N. Howling', 5362231, True)
b3 = Book('hello' , 'world', 2344323, True)
b4 = Book('T', 'H', 7568153, True)

u1 = User('Kas', 7248, [])
u2 = User('Steve', 6734, [])

library = Library([], [])
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)
library.register_user(u1)
library.register_user(u2)
# library.borrow_book(7248, 2131231)
# library.borrow_book(7248, 2131231)
# library.return_book(7248, 2131231)
# library.return_book(7248, 2131231)
# library.display_all_books()
# library.display_all_users()
# library.borrow_book(2134, 2131231)#invaild user id
# library.borrow_book(7248, 9907311)#invaild isbn
# library.return_book(8901, 2131231)#invaild user id
# library.return_book(7248, 5555788)#invaild isbn
# library.add_book(b1)#already added book
# library.register_user(u1)#already added user
# library.borrow_book(7248, 2131231)
# library.borrow_book(7248, 5362231)
# library.borrow_book(7248, 2344323)
# library.borrow_book(7248, 7568153)

continueLibrary = True
while continueLibrary == True:
	valid_user_option = False
	while valid_user_option == False:
		try:
			user_option = int(input('''Would you like to: 
1: Display all books 
2: Display all users
3: Borrow a book
4: Return a book
5: Add a new book to the library
6: Register a new user to the library
'''))
		except:
			print('Please enter a number')
			continue
		if user_option != 1 and user_option != 2 and user_option != 3 and user_option != 4 and user_option != 5 and user_option != 6:
			print('Please enter a valid number')
		else:
			valid_user_option = True

	if user_option == 1:
		library.display_all_books()
	elif user_option == 2:
		library.display_all_users()
	elif user_option == 3:
		valid_user = False
		valid_isbn = False
		while valid_user == False:
			try:
				user_id = int(input('Please enter the users id: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_user = True

		while valid_isbn == False:
			try:
				isbn = int(input('Please enter the books isbn: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_isbn = True

		library.borrow_book(user_id, isbn)
	elif user_option == 4:
		valid_user = False
		valid_isbn = False
		while valid_user == False:
			try:
				user_id = int(input('Please enter the users id: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_user = True

		while valid_isbn == False:
			try:
				isbn = int(input('Please enter the books isbn: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_isbn = True

		library.return_book(user_id, isbn)
	elif user_option == 5:
		valid_title = False
		valid_author = False
		valid_isbn = False
		while valid_title == False:
			title = str(input('Please enter the books name: '))
			if not title:
				print('Book name can not be empty')
			else:
				valid_title = True

		while valid_author == False:
			author = str(input('Please enter the author of the book: '))
			if not author:
				print('Author name can not be empty')
			else:
				valid_author = True

		while valid_isbn == False:
			try:
				isbn = int(input('Please enter the books isbn: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_isbn = True

		newBook = Book(title, author, isbn, True)
		library.add_book(newBook)

	elif user_option == 6:
		valid_name = False
		valid_id = False
		while valid_name == False:
			name = str(input('Please enter the users name: '))
			if not name:
				print('User name can not be empty')
			else:
				valid_name = True

		while valid_id == False:
			try:
				user_id = int(input('Please assign the new user an id: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_id = True

		newUser = User(name, user_id, [])
		library.register_user(newUser)


	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to select anothor option y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueLibrary = False