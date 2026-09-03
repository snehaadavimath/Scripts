# decrators in functions
# a function that takes another function as an argument,\
#  extends its behavior without explicitly modifying its \
# source code, and returns a new function

def greetDecor(func):
    def inner():
        print("Greeting from the inner function")
        func()
        print("Greetings after function call")
    return inner

@greetDecor
def greet():
    print("greetings")

# greet()


# ------------------------------------------------------------------------------------------------------------------------------------------------------


loggedIn = True

def loginRequired(func):
    def wrapper():
        if loggedIn :
            func()
            print("This is your premium account")
        else:
            print("Please login")
    return wrapper

@loginRequired
def addTocart():
    print("This is your cart")

@loginRequired
def orders():
    print("This is your orders page")

@loginRequired
def wishList():
    print("This is your wishlist page")

addTocart()

orders()

wishList()


flag=True

def loggedIn(fun):
    def warapper():
        if flag:
                print("BEfore the function call")
                fun()
                print("After the function call")
        else:
            print("flag is false")
    return warapper

@loggedIn
def logger():
    print("This is python")


logger()