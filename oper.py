a = int(input("enter the number 1: "))
b = int(input("enter the number 2: "))
c = int(input("select the operation to be performed 1. Addition 2. Subraction 3. Multiply 4. Divide : "))

# addition
if c == 1 :
    print("Result", a+b)
# subraction
elif c == 2:
    print("Result", a-b)

# multiply
elif c == 3 :
    print("Result", a*b)

# Divide
elif c == 4 :
    if a < b :
        print("A is smaller than B cannot perform the division")
    else:
        print("Result", a / b)
    
else: 
    print("Invalid option selected!")



