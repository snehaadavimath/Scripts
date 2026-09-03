# clouser function
# a nested function which retains the access even after the outer function finishes its executation

def addition(number):
    def innerAddition():
        add = number + number
        return add
    return innerAddition

sum = addition(10)

print(sum())

# -------------------------------------------------------------------------------------------------------


def outerName(name):
    

    def inner():
        print("Hello",name)
    return inner

myName = outerName("Shubham")

myName()


# -------------------------------------------------------------------------------------------------

def square(num1):

    def oper(num):
        number = num * num1
        return number
    return oper

sqr = square(2)

print(sqr(4))

# ------------------------------------------------------------------------------------------------

def cubeFun(number):

    def oper(num):
        result = num ** number
        return result
    return oper

product = cubeFun(3)

print(product(4))

