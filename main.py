# exception handling
#try:
    #a=int(input("enter the number:"))
    #print(a)
#except valueError:
    #raise valueError("invalid input.please enter a valid integer")
#finally:
    #print("hi")
def num():
    if n % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
try:
    n=int(input("enter a number"))
    num()
except ValueError:
    raise ValueError ("invalid input.please enter a valid input")
finally:
    print("bie")
