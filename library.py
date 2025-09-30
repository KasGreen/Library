class Item:
	def __init__(self, title, author, identifier, available):
		self.title = title
		self.author = author
		self.identifier = identifier
		self.available = available

	def __str__(self):
		return self.title


class Book(Item):
	def __init__(self, title, author, identifier, available):
		super().__init__(title, author, identifier, available)

	def display_book_info(self):
		print('Title: ' + self.title + '\nAuthor: ' + self.author + '\nisbn: ' + str(self.identifier))
		if self.available == True:
			print('This book is currently available\n\n')
		else:
			print('This book is currently unavailable\n\n')


class DVD(Item):
	def __init__(self, title, author, identifier, available):
		super().__init__(title, author, identifier, available)

	def display_dvd_info(self):
		print('Title: ' + self.title + '\nAuthor: ' + self.author + '\nid: ' + str(self.identifier))
		if self.available == True:
			print('This DVD is currently available\n\n')
		else:
			print('This DVD is currently unavailable\n\n')


class Magazine(Item):
	def __init__(self, title, author, identifier, available):
		super().__init__(title, author, identifier, available)

	def display_magazine_info(self):
		print('Title: ' + self.title + '\nAuthor: ' + self.author + '\nid: ' + str(self.identifier))
		if self.available == True:
			print('This magazine is currently available\n\n')
		else:
			print('This magazine is currently unavailable\n\n')



class User:
	def __init__(self, name, user_id, borrowed_items):
		self.name = name
		self.user_id = user_id
		self.borrowed_items = borrowed_items

	def borrow_item(self, item):
		if item.available == False:
			return 'unavailable'
		if len(self.borrowed_items) >= 3:
			return 'limit reached'
		self.borrowed_items.append(item)
		item.available = False
		return 'available'

	def return_item(self, item):
		if item.available == True or item not in self.borrowed_items:
			return False
		self.borrowed_items.remove(item)
		item.available = True
		return True


class Librarian(User):
	def __init__(self, name, user_id):
		super().__init__(name, user_id, None)

class Student(User):
	def __init__(self, name, user_id, borrowed_items):
		super().__init__(name, user_id, borrowed_items)

	def display_user_info(self):
		print('Name: ' + self.name + '\nUser id: ' + str(self.user_id) + '\nBorrowed books:\n')
		for i in range(0, len(self.borrowed_books)):
			print(self.borrowed_books[i])


class Library:
	def __init__(self, items, users):
		self.items = items
		self.users = users

	def add_item(self, item):
		if self.find_item(item.identifier) != None:
			print(item.title + ' is already registered in the library') 
		else:
			self.items.append(item)

	def register_user(self, user):
		if self.find_user(user.user_id) != None:
			print('The id ' + str(user.user_id) + ' is already registered to another user in the library')
		else:
			self.users.append(user)

	def find_item(self, identifier):
		for i in range(0, len(self.items)):
			item = self.items[i]
			if item.identifier == identifier:
				return item
		return None

	def find_user(self, user_id):
		for i in range(0, len(self.users)):
				user = self.users[i]
				if user.user_id == user_id:
					return user
		return None

	def borrow_item(self, user_id, identifier):
		item_to_borrow = self.find_item(identifier)
		if item_to_borrow == None:
			print(str(identifier) + ' is not a registered item in the library')
			return
		user = self.find_user(user_id)
		if user == None:
			print(str(user_id) + ' is not a registered user id')
			return
		result = user.borrow_item(item_to_borrow)
		if result == 'available':
			print(user.name + ' has borrowed ' + item_to_borrow.title)
		if result == 'unavailable':
			print(item_to_borrow.title + ' is currently unavailable')
		if result == 'limit reached':
			print(item_to_borrow.title + ' could not be borrowed since ' + user.name + ' has already borrowed 3 items')

	def return_item(self, user_id, identifier):
		item_to_return = self.find_item(identifier)
		if item_to_return == None:
			print(str(identifier) + ' is not a registered item in the library')
			return
		user = self.find_user(user_id)
		if user == None:
			print(str(user_id) + ' is not a registered user id')
			return
		result = user.return_item(item_to_return)
		if result == True:
			print(user.name + ' has returned ' + item_to_return.title)
		if result == False:
			print(item_to_return.title + ' cannot be returned')				

	def display_all_items(self):
		print('Items:\n')
		for i in range(0, len(self.items)):
			print(self.items[i])


	def display_all_users(self):
		print('Users:\n')
		for i in range(0, len(self.users)):
			print(self.users[i].name)

b1 = Book('Harry Potter', 'J. K. Rowling', 2131231, True)
b2 = Book('Barry Hopper', 'R. N. Howling', 5362231, True)
b3 = Book('hello' , 'world', 2344323, True)
b4 = Book('T', 'H', 7568153, True)

l1 = Librarian('Kas', 7248)

s1 = Student('Steve', 6734, [])
s2 = Student('Larry', 5435, [])

library = Library([], [])
library.add_item(b1)
library.add_item(b2)
library.add_item(b3)
library.add_item(b4)
library.register_user(l1)
library.register_user(s1)
library.register_user(s2)

continueLibrary = True
while continueLibrary == True:
	valid_user_option = False
	while valid_user_option == False:
		try:
			user_option = int(input('''Would you like to: 
1: Display all items 
2: Display all users
3: Borrow a item
4: Return a item
5: Add a new item to the library
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
		library.display_all_items()
	elif user_option == 2:
		library.display_all_users()
	elif user_option == 3:
		valid_user = False
		valid_identifier = False
		while valid_user == False:
			try:
				user_id = int(input('Please enter the users id: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_user = True

		while valid_identifier == False:
			try:
				identifier = int(input('Please enter the items identifier: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_identifier = True

		library.borrow_item(user_id, identifier)
	elif user_option == 4:
		valid_user = False
		valid_identifier = False
		while valid_user == False:
			try:
				user_id = int(input('Please enter the users id: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_user = True

		while valid_identifier == False:
			try:
				isbn = int(input('Please enter the items identifier: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_identifier = True

		library.return_item(user_id, identifier)
	elif user_option == 5:
		valid_title = False
		valid_author = False
		valid_identifier = False
		while valid_title == False:
			title = str(input('Please enter the items name: '))
			if not title:
				print('Item name can not be empty')
			else:
				valid_title = True

		while valid_author == False:
			author = str(input('Please enter the author of the book: '))
			if not author:
				print('Author name can not be empty')
			else:
				valid_author = True

		while valid_identifier == False:
			try:
				identifier = int(input('Please enter the items identifier: '))
			except ValueError:
				print('Please enter a number')
			else:
				valid_identifier = True

		newItem = Item(title, author, identifier, True)
		library.add_item(newItem)

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