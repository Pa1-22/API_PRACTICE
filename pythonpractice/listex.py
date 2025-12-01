#create the list using square brackets

'''mylist=["apple","banana","cat","xerox"]

newlist=["basket","hall","gear"]

mylist.append(newlist)
mylist.extend(newlist)

print(mylist)
'''
#create a tuple using open brackets
# lambda function doent need a name 
 
# List of employees with their names and salaries
from functools import reduce

# Using reduce() to multiply all elements in the list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24