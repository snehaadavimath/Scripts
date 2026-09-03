# Reverse a string using a loop.

string = 'Today is a great day for me'

reverString = ''

for char in string :
    reverString = char + reverString

print("The Reversed String is: ",reverString)

# Count the number of characters in a string without using len().

car = 'mahindra'
count = 0

for char in car:
    count += 1;

print("The characters in string is: ", count)


# Count the number of vowels in a string.

stringVowels = ' Count the number of vowels in a string'
v = 'a,e,i,o,u'
counter = 0

for vowels in stringVowels:
    if vowels in v:
        counter += 1

print("Number of vowels in given string is: ",counter)

# Find the largest number in a list.
# Find the smallest number in a list.
numList = [1,50,10,30,60]

numList.sort()

print(numList)

# biggest number in list

print(numList[-1])

# smallest number of list

print(numList[0])

# Calculate the average of numbers in a list.
avrageList = sum(numList) / len(numList)

print(avrageList)

# Count positive and negative numbers in a list.
positiveCounter = 0
negativeCounter = 0
for element in numList : 
    if element >= 0 :
        positiveCounter += 1;
    else : 
        negativeCounter += 1;

print(f"There are {positiveCounter} positive numbers")
print(f"There are {negativeCounter} negative numbers")


# Remove duplicate values from a list without using a set.

dupList = [5,3,6,2,5,8,6]
uniqueList = []

for element in dupList:
    if element not in uniqueList:
        uniqueList.append(element)

print("the original list", dupList);
print("the unique List", uniqueList)

# Count the frequency of each character in a string.

name = "powershell"
frequency = {}

for char in name:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print (frequency)

# Count the frequency of each element in a list.

list = [1,1,1,2,2,25,5,5,5,3,3,3]

result = ''
visited=[]

for element in list:
    if element not in visited:
        result += str(element) + str(list.count(element))
        visited.append(element)

print(result)


# Check whether a number is an Armstrong number. 153, 9474

def isArmstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

number = int(input("enter a number: "))
if isArmstrong(number):
    print(f"the given number {number} is Armstrong number")
else:
    print(f"the given number {number} is not Armstrong number")


# Read marks of multiple students and display Pass/Fail for each student

students = {
    "Samkisha" : 74,
    "Samskart" : 28,
    "Nimitha" : 92,
    "Vanshika" : 45
      }

for name , marks in students.items():
    if marks > 35 :
        print(name, " you are Pass")
    else:
        print(name, " Sorry you are Fail")


# Store employee names and salaries. Display employees \
# whose salary is greater than a given amount. Hint: Use a dictionary.

employees = {}

empDetails = int(input("Enter the number of employee details you want to enter: "))

for i in range(empDetails) :
    name = input("Enter the name of the employee: ")
    salary = int(input("Enter the salary of the employee: "))

    employees[name] = salary

for name , salary in employees.items() :
    if salary > 5000:
        print(f"the employee {name} has greater {salary}")


