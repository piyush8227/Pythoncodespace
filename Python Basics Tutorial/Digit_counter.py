'''
Author: Piyush More
Description: Counting digits in a file.
'''

# Inserting data in file.
file = open("Task.txt", 'w')

data = '''1 1 1 1 1
2 2 2 2
3 3 3 3 3 3
4 4 4
5
'''

file.write(data)

file.close()

# Checking or printing data.

file = open('Task.txt', 'r')

data = file.read()

print(data)

file.close()

# Finding and counting digit.

digit = input("Enter a digit: ")

counts = data.count(digit)

print("Count of digit in file is:", counts)

