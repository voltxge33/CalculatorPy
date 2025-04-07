import math
def add():
    numb1 = input("First# ")
    numb2 = input("Second# ")
    try:
        print(f"{float(numb1) + float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def subtract():
    numb1 = input("First# ")
    numb2 = input("Second# ")
    try:
        print(f"{float(numb1) - float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def multiply():
    numb1 = input("First# ")
    numb2 = input("Second# ")
    try:
        print(f"{float(numb1) * float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def divide():
    numb1 = input("First# ")
    numb2 = input("Second# ")
    try:
        print(f"{float(numb1) / float(numb2)}")
    except ValueError:
        print("Error, Non-floats Entered")
def sqrt():
    numb1 = input("#: ")

    try:
        result = math.sqrt(float(numb1))
        print(f"{result}")
    except ValueError:
        print("Error, Non-float or negative number entered.")
def square():

    numb1 = input("#: ")
    try:
        print(f"{float(numb1) ** 2}")
    except ValueError:
        print("Error, Non-float Entered")
def exp():
    numb1 = input("#: ")
    numb2 = input("Exponent: ")
    try:
        print(f"{float(numb1) ** float(numb2)}")
    except ValueError:
        print("Error, Non-float Entered")
def vertex():
    try:
        a = float(input("a value "))
        b = float(input("b value "))
        c = float(input("c value "))
        x_vertex = (-1 * b)/(2 * a)
        y_vertex = (a * x_vertex ** 2) + (b * x_vertex) + c
        print(f'Vertex: ({x_vertex}, {y_vertex})')
    except ValueError:
        print("Error, Non-float Entered")
def convert():
    pass
