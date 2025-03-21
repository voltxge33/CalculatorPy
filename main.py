import calcfunctions
def calculator():
    while True:
        calctype = input("add, subtract, multiply, divide, sqrt, square, exponent: ")
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
            case "exponent":
                calcfunctions.exp()
            case _:
                print("Error, incorrect case")



while True:
    maintype = input("What job(calc, convert, vertex) ")
    match maintype:
        case "calc":
            calculator()
        case "convert":
            calcfunctions.convert()
        case "vertex":
            calcfunctions.vertex()
        case _:
            print("Error")