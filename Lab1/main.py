import utilities

print("Hello world")

# check calc func
while True:
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        break
    except ValueError:
        print("Incorrect input! Try again: ")

while True:
    operation = input("Enter operation(add, sub, mult, div): ")
    result = utilities.calc(num1, num2, operation)
    if result != "Incorrect operator":
        print("Result:", result)
        break
    else:
        print(result)

# check even list function
while True:
    try:
        length = int(input("Input length of list: "))
        break
    except ValueError:
        print("Incorrect input! Try again: ")

lst = []
for i in range(length):
    while True:
        try:
            item = int(input("Input item " + str(i) + " of list: "))
            lst.append(item)
            break
        except ValueError:
            print("Incorrect input! Try again: ")

print(utilities.get_even_number_list(lst))
