# syntax error

# A syntax error occurs when Python doesn’t recognize a section of your program as valid Python code
# For example, if you use an apostrophe within 
# single quotes, you’ll produce an error. This happens because Python interprets everything between the first single quote and the apostrophe as a 
# string. It then tries to interpret the rest of the text as Python code, which 
# causes errors.

# Here’s how to use single and double quotes correctly. Save this program 
# as apostrophe.py and then run it:

message = "One of Python's strengths is its diverse community."
print(message)

# The apostrophe appears inside a set of double quotes, so the Python 
# interpreter has no trouble reading the string correctly


# if you use single quotes, Python can’t identify where the string 
# should end

# message = 'One of Python's strengths is its diverse community.'
# print(message)

# You’ll see the following output:

#  File "apostrophe.py", line 21
#  message = 'One of Python's strengths is its diverse community.'
# SyntaxError: unterminated string literal (detected at line 1)