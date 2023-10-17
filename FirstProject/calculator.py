firstNumber = int(input("Ingrese un número: "))
secondNumber = int(input("Ingrese otro número: "))
operation = input("Ingrese un operador (+, -, *, /): ")

match operation:
    case "+":
        print(firstNumber + secondNumber)
    case "-":
        print(firstNumber - secondNumber)
    case "*":
        print(firstNumber * secondNumber)
    case "/":
        print(firstNumber / secondNumber)
