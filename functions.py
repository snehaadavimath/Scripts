# Write a function to print "Hello, Python!".

def displayHello():
    print("hello")
    

displayHello()

# Write a function that accepts a name and prints a welcome message

def greetings(name):
    print(f"welcome {name} for today's meeting!!")
    

personName = input("enter a your name: ")

greetings(personName)

# Write a function to add two numbers.
# Write a function to subtract two numbers.
# Write a function to multiply two numbers.
# Write a function to divide two numbers.

def addition(number1 , number2):
    total = number1 + number2
    print(f"The sum of given numbers {number1} and {number2} is : " , total)
    

def subraction(number1 , number2):
    total = number1 - number2
    print(f"The difference of given numbers {number1} and {number2} is : " , total)
  

def multiply(number1 , number2):
    total = number1 * number2
    print(f"The product of given numbers {number1} and {number2} is : " , total)
   

def divide(number1 , number2):
    quotient = number1 / number2 
    reminder = number1 % number2
    print(f"The Quotient of given numbers {number1} and {number2} is : {quotient} and the Reminder is {reminder}" )
    

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
selector = int(input("select the operation you want to perform 1.Addition 2.Subraction 3.Multiply 4.Division: "))


if selector == 1:
    addition(num1,num2)
elif selector ==2 :
    subraction(num1,num2)
elif selector == 3:
    multiply(num1,num2)
elif selector == 4:
    divide(num1,num2)
else:
    print("Invalid option selected")


# Write a function that returns the largest of two numbers.
# Write a function that returns the smallest of two numbers.

def largest(a , b):
    if a > b :
        return a
    else:
        return b

def smallest(a , b):
    if a < b:
        return a
    else:
        return b
    
a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))

result = largest(a,b)
smallerResult = smallest(a , b)

print("The largest Number is: ", result)
print("The smaller number is : ", smallerResult)



