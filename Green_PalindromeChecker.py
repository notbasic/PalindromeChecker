
class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass

class Stack:
	"""LIFO Stack implementation using a Python list as underlying storage."""

	def __init__ (self):
		"""Create an empty stack."""
		self._data = [ ] # nonpublic list instance

	def __len__(self):
		"""Return the number of elements in the stack."""
		return len(self._data)

	def is_empty(self):
		"""Return True if the stack is empty."""
		return len(self) == 0

	def push(self, e):
		"""Add element e to the top of the stack."""
		self._data.append(e)	# new item stored at end of list

	def top(self):
		"""Return (but do not remove) the element at the top of the stack. Raise Empty exception if the stack is empty. """
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1] # the last item in the list

	def pop(self):
		"""Remove and return the element from the top of the stack (i.e., LIFO). Raise Empty exception if the stack is empty. """
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop( )	# remove last item from list

	def __str__(self):

		str_repr = ""
		for el in self._data:
			str_repr +=str(el) + "\n"
		str_repr = "".join(reversed(str_repr.strip()))

		return str_repr

def stackify():
	sentence = input("Please enter a sentence: ")
	s = Stack()
	for c in sentence:
		s.push(c)

	print()
	print(sentence,end = " ")

	return s

# -------------------------- DO NOT MODIFY ANYTHING ABOVE THIS LINE ----------------

def flip_flop():
	p = Stack()  # created a new stack
	is_palindrone = None     #initalized to none
	word = input('test a word for is_palindrone:')    # collect a test object
	p.push(word)      # pushed it to the stack
	if str(p).lower() == str(p.pop()).lower():     # tested if it is a palindrone or not
		is_palindrone = print(word, ' is a palindrome ')
	else:
		is_palindrone = print(word, 'is not a palindrome')
	return is_palindrone

flip_flop()     # function call
