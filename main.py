import calcfunctions


def calculator():
    calctype = input("add, subtract, multiply, divide, sqrt, square: ")
    match calctype:
        case "add":
            calcfunctions.add()
        case "subtract":
            calcfunctions.subtract()
        case "multiply":
            calcfunctions.multiply()
        case "divide":
            calcfunctions.divide()
        case "sqrt":
            calcfunctions.sqrt()
        case "square":
            
            calcfunctions.square()
        case _:
            print("Error, incorrect case")
calculator()