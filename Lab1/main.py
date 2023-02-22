import utilities

print("Hello world")
while True:
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
    except ValueError:
        print("Incorrect input! Try again: ")
    else:
        while True:
            operation = input("Enter operation(add, sub, mult, div): ")
            result = utilities.calc(num1, num2, operation)
            if result != "Incorrect operator":
                print("Result:", result)
                break
            else:
                print(result)
        break
