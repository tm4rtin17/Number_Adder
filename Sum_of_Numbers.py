import pyinputplus as pyip

#Takes user input, positive numbers only
number = pyip.inputNum("What number do you want to add?", min=0)
total = 0

#Iterates over every number in the range; Example (user enters 3): 1 + 2 + 3 = 6
for i in range(number + 1):
    total += i

#Prints the total
print(f'The sum of all numbers from 1 to {number} is {total}.')
