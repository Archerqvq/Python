# A string is a series of characters. Anything inside quotes is considered 
# a string in Python, and you can use single or double quotes around your 
# strings like this:

# "This a string."
# 'This a string.'

# This flexibility allows you to use quotes and apostrophes within your 
# strings:

# 'I told my friend, "Python is my favorite language!"'
# "The language 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."

# A method is an action that Python can perform on a piece of data. The dot (.) 
# after name in name.title() tells Python to make the title() method act on 
# the variable name.
# Every method is followed by a set of parentheses, because 
# methods often need additional information to do their work. That information is provided inside the parentheses. The title() function doesn’t need 
# any additional information, so its parentheses are empty

name = "ada lovelace"
print(name.title())

# As the same as below
print(str.title(name))

# Change a string to all uppercase or all lowercase
print(name.upper())
print(name.lower())