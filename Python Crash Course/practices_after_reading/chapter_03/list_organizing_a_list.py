# Organizing a List
## Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# The sort() method changes the order of the list permanently. The cars 
# are now in alphabetical order, and we can never revert to the original order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

## Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

## Printing a List in Reverse Order
# Notice that reverse() doesn’t sort backward alphabetically; it simply 
# reverses the order of the list:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

## Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
