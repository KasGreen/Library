class Item:
	def __init__(self, title, author, identifier, available, limit, duration, fine):
		self.title = title
		self.author = author
		self.identifier = identifier
		self.available = available
		self.limit = limit
		self.duration = duration
		self.fine = fine

	def __str__(self):
		return self.title

	def display_title(self):
		print(self.title)

	def display_title_and_identifier(self):
		print(self.title + ' (' + str(self.identifier) + ')')


class Book(Item):
	def __init__(self, title, author, identifier, available):
		super().__init__(title, author, identifier, available, 3, 21, 0.25)

	def display_book_info(self):
		print('Title: ' + self.title + '\nAuthor: ' + self.author + '\nisbn: ' + str(self.identifier))
		if self.available == True:
			print('This book is currently available\n\n')
		else:
			print('This book is currently unavailable\n\n')

class DVD(Item):
	def __init__(self, title, author, identifier, available):
		super().__init__(title, author, identifier, available, 2, 7, 0.5)

	def display_dvd_info(self):
		print('Title: ' + self.title + '\nAuthor: ' + self.author + '\nid: ' + str(self.identifier))
		if self.available == True:
			print('This DVD is currently available\n\n')
		else:
			print('This DVD is currently unavailable\n\n')

class Magazine(Item):
	def __init__(self, title, author, identifier, available):
		super().__init__(title, author, identifier, available, 5, 14, 0.2)

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
		self.item_days_left = {}

	def count_borrowed_books(self):
		count = 0
		for i in range(0, len(self.borrowed_items)):
			if type(self.borrowed_items[i]) is Book:
				count += 1
		return count

	def count_borrowed_magazines(self):
		count = 0
		for i in range(0, len(self.borrowed_items)):
			if type(self.borrowed_items[i]) is Magazine:
				count += 1
		return count

	def count_borrowed_dvds(self):
		count = 0
		for i in range(0, len(self.borrowed_items)):
			if type(self.borrowed_items[i]) is DVD:
				count += 1
		return count

	def borrow_item(self, item):
		if item.available == False:
			return 'unavailable'
		if type(item) == Book:
			if self.count_borrowed_books() >= item.limit:
				return 'limit reached'
		if type(item) == Magazine:
			if self.count_borrowed_magazines() >= item.limit:
				return 'limit reached'
		if type(item) == DVD:
			if self.count_borrowed_dvds() >= item.limit:
				return 'limit reached'
		self.borrowed_items.append(item)
		self.item_days_left[item.identifier] = item.duration
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
		total_fine = 0
		print('Borrowed items:\n')
		for i in range(0, len(self.borrowed_items)):
			days_left = self.item_days_left[self.borrowed_items[i].identifier]
			if days_left >= 0:
				print(self.borrowed_items[i].title + ' (' + str(self.borrowed_items[i].identifier) + ') ' + 'Days left - ' + str(days_left))
			else:
				fine = self.calculate_item_fine(self.calculate_overdue_days(days_left), self.borrowed_items[i].fine)
				print(self.borrowed_items[i].title + ' (' + str(self.borrowed_items[i].identifier) + ') ' + 'Days overdue - ' + str(days_left * -1) + ' Fine = ' + format(fine, ".2f") )
				total_fine = total_fine + fine
		if total_fine > 0:
			print('Your total fine is' + ' ' + format(total_fine, ".2f"))
		print('')

	def calculate_item_fine(self, overdue_days, fine_per_day):
		total_fine = overdue_days * fine_per_day
		return round(total_fine,2)

	def calculate_overdue_days(self, days):
		if days >= 0:
			return 0
		return -1 * days



	def has_borrowed_items(self):
		if len(self.borrowed_items) == 0:
			return False
		return True


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

	def get_item_and_student(self, student_id, identifier):
		student = self.find_student(student_id)
		if student == None:
			print(str(student_id) + ' is not a registered student id')
			return student, None
		item = self.find_item(identifier)
		if item == None:
			return student, item

		return student, item

	def borrow_item(self, student_id, identifier):
		student, item_to_borrow = self.get_item_and_student(student_id, identifier)
		if student == None:
			return
		if item_to_borrow == None:
			print(str(identifier) + ' is not a registered item in the library')
			return
		result = student.borrow_item(item_to_borrow)
		if result == 'available':
			print(student.name + ' has borrowed ' + item_to_borrow.title)
		if result == 'unavailable':
			print(item_to_borrow.title + ' is currently unavailable')
		if result == 'limit reached':
			print(item_to_borrow.title + ' could not be borrowed since ' + student.name + ' has already borrowed ' + str(item_to_borrow.limit) + ' ' + item_to_borrow.__class__.__name__)

	def return_item(self, student_id, identifier):
		student, item_to_return = self.get_item_and_student(student_id, identifier)
		if student == None:
			return
		if item_to_return == None:
			print(student.name + ' has not borrowed an item with this ID')
			return
		result = student.return_item(item_to_return)
		if result == True:
			print(student.name + ' has returned ' + item_to_return.title)
		if result == False:
			print(item_to_return.title + ' cannot be returned')				

	def display_all_books(self):
		print('Books(Must be returned after 3 weeks - 25p fine per day late):\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Book:
				self.items[i].display_title_and_identifier()
		print('')

	def display_all_magazines(self):
		print('Magazines(Must be returned after 2 weeks - 20p fine per day late):\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Magazine:
				self.items[i].display_title_and_identifier()
		print('')

	def display_all_dvds(self):
		print('Dvds(Must be returned after 1 week - 50p fine per day late):\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is DVD:
				self.items[i].display_title_and_identifier()
		print('')

	def display_all_available_items(self):
		book_count = 0
		print('Books(Must be returned after 3 weeks - 25p fine per day late):\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Book and self.items[i].available == True:
				self.items[i].display_title_and_identifier()
				book_count += 1
		if book_count == 0:
			print('There are no available books')
		mag_count = 0
		print('\nMagazines(Must be returned after 2 weeks - 20p fine per day late):\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is Magazine and self.items[i].available == True:
				self.items[i].display_title_and_identifier()
				mag_count += 1
		if mag_count == 0:
			print('There are no available magazines')
		dvd_count = 0
		print('\nDvds(Must be returned after 1 week - 50p fine per day late):\n')
		for i in range(0, len(self.items)):
			if type(self.items[i]) is DVD and self.items[i].available == True:
				self.items[i].display_title_and_identifier()
				dvd_count += 1
		if dvd_count == 0:
			print('There are no available DVDs')
		print('')

	def has_available_items(self):
		if len(self.items) == 0:
			return False
		for i in range(0, len(self.items)):
			if self.items[i].available == True:
				return True
		return False

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

def moveDaysForward(days):
	for i in range(0, len(library.users)):
		if type(library.users[i]) is Student:
			for key in library.users[i].item_days_left:
				library.users[i].item_days_left[key] -= days
			

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
13: Move day forward
14: Move 10 days forward
'''))
		except:
			print('Please enter a number')
			continue
		if user_option < 1 or user_option > 14:
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
		if library.has_available_items() == True:
			student_id = studentID_input()
			if library.find_student(student_id) != None:
				library.display_all_available_items()
				identifier = itemIdentifier_input()
				library.borrow_item(student_id, identifier)
			else:
				print('There is no student with this ID')
		else:
			print('The library currently has no available items')
	elif user_option == 7:
		student_id = studentID_input()
		student = library.find_student(student_id)
		if student != None:
			if student.has_borrowed_items() == True:
				student.display_borrowed_items()
				identifier = itemIdentifier_input()
				library.return_item(student_id, identifier)
			else:
				print(student.name + ' has no items to return')
		else:
			print('There is no student with this ID')
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

	elif user_option == 13:
		moveDaysForward(1)

	elif user_option == 14:
		moveDaysForward(10)

	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to select anothor option y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueLibrary = False