from random import *

def getRandList(numOfItemsInList, startRange = 1, endRange = 150):
    myList = []
    for val in range(numOfItemsInList):
        myList.append(randint(startRange, endRange))

    return myList

# Merge two dictionaries
########################
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
#
# # first method
# print({**d1, **d2})
#
# # second method
# d1.update(d2)
# print(d1)


# Map two lists into a dictionary
################
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# mapped = {}
#
# for val in range(3):
#     mapped[keys[val]] = values[val]
#
# print(mapped)

# Extend a list without append
##################
# x = [10, 20, 30]
# y = [40, 50, 60]
# # using slicing - https://stackoverflow.com/a/2947881/3283425
# x[3:] = y
# print(x)

# Get the largest number from a list
##################

# biggest = 0
# nums = [3, 7, 1, 7, 13, 25, 33, 12, 1]
#
# for num in nums:
#     if num > biggest:
#         biggest = num
#
# print(biggest)

# Sum all the items in a list
##################
# nums = [3, 7, 1, 7, 13, 25, 33, 12, 1]
# sum = 0
#
# for num in nums:
#     sum += num
#
# print(sum)

# Iterate over two lists simultaneously
##################

# a = getRandList(10)
# b = getRandList(10)
#
# print('First list: ', a, '\n', 'Second list: ', b)
#
# # let's iterate over the zipped items
# for aItem,bItem in zip(a, b):
#     print("Item from a list is {0} and item from b list is {1}".format(aItem, bItem))

# Find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
##################
myList = getRandList(20, 1000, 4000)

for num in myList:
    if (num >= 1500 and num <= 2700 and
     num % 7 == 0 ):
        print(num)
