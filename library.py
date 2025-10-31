class Item:
	def __init__(self, title, author, identifier, available):
		self.title = title
		self.author = author
		self.identifier = identifier
		self.available = available

	def __str__(self):
		return self.title

	def display_title(self):
		print(self.title)

	def display_title_and_identifier(self):
		print(self.title + ' (' + str(self.identifier) + ')')


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

	def display_name(self):
		print(self.name)

	def display_name_and_Id(self):
		print(self.name + ' (' + str(self.user_id) + ')')

class Librarian(User):
	def __init__(self, name, user_id):
		super().__init__(name, user_id, None)

class Student(User):
	def __init__(self, name, user_id, borrowed_items):
		super().__init__(name, user_id, borrowed_items)

	def display_borrowed_items(self):
		print('Borrowed items:\n')
		for i in range(0, len(self.borrowed_items)):
			print(self.borrowed_items[i].title + ' (' + str(self.borrowed_items[i].identifier) + ')')
		print('')

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

	def find_item(self, identifier):
		for i in range(0, len(self.items)):
			item = self.items[i]
			if item.identifier == identifier:
				return item
		return None

	def find_book(self, identifier):
		for i in range(0, len(self.items)):
			item = self.items[i]
			if item.identifier == identifier and type(item) is Book:
				return item
		return None

	def add_book(self, item):
		if self.find_book(item.identifier) != None:
			print(item.title + ' is already registered in the library') 
		else:
			self.items.append(item)

	def find_magazine(self, identifier):
		for i in range(0, len(self.items)):
			item = self.items[i]
			if item.identifier == identifier and type(item) is Magazine:
				return item
		return None

	def add_magazine(self, item):
		if self.find_magazine(item.identifier) != None:
			print(item.title + ' is already registered in the library') 
		else:
			self.items.append(item)

	def find_dvd(self, identifier):
		for i in range(0, len(self.items)):
			item = self.items[i]
			if item.identifier == identifier and type(item) is DVD:
				return item
		return None

	def add_dvd(self, item):
		if self.find_dvd(item.identifier) != None:
			print(item.title + ' is already registered in the library') 
		else:
			self.items.append(item)

	def find_student(self, user_id):
		for i in range(0, len(self.users)):
			user = self.users[i]
			if user.user_id == user_id and type(user) is Student:
				return user
		return None

	def register_student(self, user):
		if self.find_student(user.user_id) != None:
			print('The id ' + str(user.user_id) + ' is already registered to another student in the library')
		else:
			self.users.append(user)

	def find_librarian(self, user_id):
		for i in range(0, len(self.users)):
			user = self.users[i]
			if user.user_id == user_id and type(user) is Librarian:
				return user
		return None

	def register_librarian(self, user):
		if self.find_librarian(user.user_id) != None:
			print('The id ' + str(user.user_id) + ' is already registered to another librarian in the library')
		else:
			self.users.append(user)

	def get_item_and_student(self):
		item = self.find_item(identifier)
		if item == None:
			print(str(identifier) + ' is not a registered item in the library')
			return
		student = self.find_student(student_id)
		if student == None:
			print(str(student_id) + ' is not a registered student id')
			return

		return item, student

	def borrow_item(self, student_id, identifier):
		item_to_borrow, student = self.get_item_and_student()
		result = student.borrow_item(item_to_borrow)
		if result == 'available':
			print(student.name + ' has borrowed ' + item_to_borrow.title)
		if result == 'unavailable':
			print(item_to_borrow.title + ' is currently unavailable')
		if result == 'limit reached':
			print(item_to_borrow.title + ' could not be borrowed since ' + student.name + ' has already borrowed 3 items')

	def return_item(self, student_id, identifier):
		item_to_return, student = self.get_item_and_student()
		result = student.return_item(item_to_return)
		if result == True:
			print(student.name + ' has returned ' + item_to_return.title)
		if result == False:
			print(item_to_return.title + ' cannot be returned')				

	def display_all_books(self):
		print('Books:\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Book:
				self.items[i].display_title_and_identifier()
		print('')

	def display_all_magazines(self):
		print('Magazines:\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Magazine:
				self.items[i].display_title_and_identifier()
		print('')

	def display_all_dvds(self):
		print('Dvds:\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is DVD:
				self.items[i].display_title_and_identifier()
		print('')

	def display_all_available_items(self):
		print('Books:\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Book and self.items[i].available == True:
				self.items[i].display_title_and_identifier()
		print('\nMagazines:\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Magazine and self.items[i].available == True:
				self.items[i].display_title_and_identifier()
		print('\nDvds:\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is DVD and self.items[i].available == True:
				self.items[i].display_title_and_identifier()
		print('')


	def display_all_students(self):
		print('Students:')
		for i in range(0, len(self.users)):
			if type(self.users[i]) is Student:
				self.users[i].display_name_and_Id()
		print('')

	def display_all_librarians(self):
		print('Librarians:')
		for i in range(0, len(self.users)):
			if type(self.users[i]) is Librarian:
				self.users[i].display_name_and_Id()
		print('')

def inputItem():
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
		author = str(input('Please enter the authors name: '))
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

	return title, author, identifier

def inputUser():
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

		return name, user_id

def studentID_input():
	valid_user = False
	library.display_all_students()
	while valid_user == False:
		try:
			student_id = int(input('Please enter the students id: '))
		except ValueError:
			print('Please enter a number')
		else:
			valid_user = True
	return student_id

def itemIdentifier_input():
	valid_identifier = False
	while valid_identifier == False:
		try:
			identifier = int(input('Please enter the items identifier: '))
		except ValueError:
			print('Please enter a number')
		else:
			valid_identifier = True
	return identifier
			

b1 = Book('Harry Potter', 'J. K. Rowling', 2131231, True)
b2 = Book('Barry Hopper', 'R. N. Howling', 5362231, True)
b3 = Book('book3' , 'world', 2344323, True)
b4 = Book('book4', 'H', 7568153, True)

m1 = Magazine('mag1', 'n', 123, True)
m2 = Magazine('mag2', 'g', 321, True)

d1 = DVD('DVD1', 'J', 987, True)
d2 = DVD('DVD2', 'L', 789, True)

l1 = Librarian('Kas', 7248)

s1 = Student('Steve', 6734, [])
s2 = Student('Larry', 5435, [])

library = Library([], [])
library.add_item(b1)
library.add_item(b2)
library.add_item(b3)
library.add_item(b4)
library.add_item(m1)
library.add_item(m2)
library.add_item(d1)
library.add_item(d2)
library.register_librarian(l1)
library.register_student(s1)
library.register_student(s2)

continueLibrary = True
librarian_id = int(input('Please enter your librarian id '))
librarian = library.find_librarian(librarian_id)
if librarian == None:
	print(str(librarian_id) + ' is not a registered librarian id')
	continueLibrary = False
while continueLibrary == True:
	valid_user_option = False
	while valid_user_option == False:
		try:
			user_option = int(input('''Would you like to: 
1: Display all books
2: Display all magazines
3: Dispaly all dvds
4: Display all students
5: Display all Librarians
6: Borrow a item
7: Return a item
8: Add a new book to the library
9: Add a new magazine to the library
10: Add a new DVD to the library
11: Register a new student to the library
12: Register a new librarian to the library
'''))
		except:
			print('Please enter a number')
			continue
		if user_option != 1 and user_option != 2 and user_option != 3 and user_option != 4 and user_option != 5 and user_option != 6 and user_option != 7 and user_option != 8 and user_option != 9 and user_option != 10 and user_option != 11 and user_option != 12:
			print('Please enter a valid number')
		else:
			valid_user_option = True

	if user_option == 1:
		library.display_all_books()
	elif user_option == 2:
		library.display_all_magazines()
	elif user_option == 3:
		library.display_all_dvds()
	elif user_option == 4:
		library.display_all_students()
	elif user_option == 5:
		library.display_all_librarians()
	elif user_option == 6:
		student_id = studentID_input()
		library.display_all_available_items()
		identifier = itemIdentifier_input()

		library.borrow_item(student_id, identifier)
	elif user_option == 7:
		student_id = studentID_input()
		student = library.find_student(student_id)
		student.display_borrowed_items()
		identifier = itemIdentifier_input()

		library.return_item(student_id, identifier)
	elif user_option == 8:
		title,author,identifier = inputItem()

		newBook = Book(title, author, identifier, True)
		library.add_book(newBook)

	elif user_option == 9:
		title,author,identifier = inputItem()

		newMagazine = Magazine(title, author, identifier, True)
		library.add_magazine(newMagazine)

	elif user_option == 10:
		title,author,identifier = inputItem()

		newDVD = DVD(title, author, identifier, True)
		library.add_dvd(newDVD)

	elif user_option == 11:
		name,user_id = inputUser()

		newStudent = Student(name, user_id, [])
		library.register_student(newStudent)

	elif user_option == 12:
		name,user_id = inputUser()

		newLibraian = Librarian(name, user_id)
		library.register_librarian(newLibraian)


	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to select anothor option y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueLibrary = False