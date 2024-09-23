# In programming, whitespace refers to any nonprinting characters, such as 
# spaces, tabs, and end-of-line symbols. You can use whitespace to organize 
# your output so it’s easier for users to read.

# Stripping Whitespace
# 'python' and 'python ' look pretty much the same. But to a program, they 
# are two different strings. Python detects the extra space in 'python ' and 
# considers it significant unless you tell it otherwise.

favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.lstrip()
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)