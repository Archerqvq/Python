# In Python, square brackets ([]) indicate a list, and individual elements 
# in the list are separated by commas. Here’s a simple example of a list that 
# contains a few kinds of bicycles:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

################################

# Accessing Elements in a List

# Lists are ordered collections, so you can access any element in a list by 
# telling Python the position, or index, of the item desired.
# To access an element in a list, write the name of the list followed by the index of the item 
# enclosed in square brackets.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
# Python considers the first item in a list to be at position 0, not position 1.
print(bicycles[1])
print(bicycles[3])

# Python has a special syntax for accessing the last element in a list. If you 
# ask for the item at index -1, Python always returns the last item in the list:
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])


################################

# Using Individual Values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


################################

# Modifying, Adding, and Removing Elements
## Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

## Adding Elements to a List
### Appending Elements to the End of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For example, 
# you can start with an empty list and then add items to the list using a series 
# of append() calls. Using an empty list, let’s add the elements 'honda', 'yamaha', 
# and 'suzuki' to the list:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

### Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

### Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

### Removing an Item Using the pop() Method
#   Sometimes you’ll want to use the value of an item after you remove it from a 
# list. For example, you might want to get the x and y position of an alien that 
# was just shot down, so you can draw an explosion at that position. In a web 
# application, you might want to remove a user from a list of active members 
# and then add that user to a list of inactive members.
#   The pop() method removes the last item in a list, but it lets you work 
# with that item after removing it. The term pop comes from thinking of a 
# list as a stack of items and popping one item off the top of the stack. In this 
# analogy, the top of a stack corresponds to the end of a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

### Popping Items from Any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

### Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove 
# from a list. If you only know the value of the item you want to remove, you 
# can use the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# The remove() method deletes only the first occurrence of the value you specify. If there’s 
# a possibility the value appears more than once in the list, you’ll need to use a loop 
# to make sure all occurrences of the value are removed