import math
def add():
    numb1 = input("first# ")
    numb2 = input("second# ")
    try:
        print(f"{float(numb1) + float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def subtract():
    numb1 = input("first# ")
    numb2 = input("second# ")
    try:
        print(f"{float(numb1) - float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def multiply():
    numb1 = input("first# ")
    numb2 = input("second# ")
    try:
        print(f"{float(numb1) * float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def divide():
    numb1 = input("first# ")
    numb2 = input("second# ")
    try:
        print(f"{float(numb1) / float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def sqrt():
    numb1 = input("first# ")

    try:
        result = math.sqrt(float(numb1))
        print(f"{result}")
    except ValueError:
        print("Error, Non-float or negative number entered.")
def square():

    numb1 = input("first# ")
    try:
        print(f"{float(numb1) ** 2}")
    except ValueError:
        print("Error, Non-float Entered")
def exp():
    numb1 = ("Number: ")
    numb2 = ("Exponent: ")
    try:
        print(f"{numb1 ** numb2}")
    except ValueError:
        print("Error, Non-float Entered")