def calc(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mult":
        return num1 * num2
    elif operation == "div":
        return num1 / num2 if num2 != 0 else "Cannot divided by zero"
    else:
        return "Incorrect operator"
