# Python example - Edward Ayala

# <- This is a comment
"""
This can be considered a block comment in Python
There is no 'official' syntax for block comments
but this is a creative way to implement block comments
"""
# This is another way
# to implement block comments
# unfortunatly there isn't an official method 
# but it works I guess

# Declaring / Initializing variables
a = 0
b = 0.0
c = ""
d = False

# Conditional statement
if a > 1:
	d = True
elif b < 5:
	d = True
else:
	d = False

print("Boolean example: ", d)
print() #Line break?

# Intersting note: can only concat string and string
# to concat string and other datatype we can use:
# "{} and {}.format("string",data) or just use print("string",data)

def mathExample(a, b):
	print("mathExample: build numbers, do math, output answers")
	# Loop to build int
	for i in range(10):
		a += 2
	print("{}: {}".format("Integer a", a))
	
	# Loop to build double
	for i in range(10):
		b += 1.5
	print("{}: {}".format("Double b", b))
	
	# Math operations
	print("SUM:", a+b)
	print("PRODUCT:", a*b)
	print("QUOTIENT:", a/b)
	print("POWER:", pow((a+b),2))
	print("AVERAGE:", (a+b)/2)
	print("MODULUS:", a%b)
	
# Function call	
mathExample(a,b) # Interesting note: function call must be after function definition
print()

def stringExample(s):
	print("stringExample: build string, split string, get character at index, conditional test for string")
	
	# Strings can be built or concatenated using many methods, the simplest is using the + symbol
	s = " This "+"string "+"was "+"created "+"using "+"concatenation."
	print("We built this string ->" + s)
	
	# split string / Array example
	strArray = s.split(" ")
	for i in strArray:
		print(i)
	
	# Index value of string
	print("\nThe character at index 11: " + s[10]) # No need for String.charAt() like Java
	# Conditional test for string
	print("Does the string contain the word cat?", "cat" in s)
	
# Function call	
stringExample(c)
print()

# Declaring a class
class classExample:
	# Initializing class object
	def __init__(self,n,s):
		self.num = n
		self.string = s
	# Class method
	def numFunction(self):
		for i in range(15):
			self.num = self.num * 2
			self.num = self.num - 3
		print("numFunction(in class method): ", self.num)
	# Class method
	def strFunction(self):
		print("\nstrFunction(in class method):",self.string)
		print("This is the character at index 8: ", self.string[8])
		print("Does this string contain the word ring?", "ring" in self.string)

# Creating class object	
objEx = classExample(5,"This is a string.")

# Class method calls
objEx.numFunction()
objEx.strFunction()