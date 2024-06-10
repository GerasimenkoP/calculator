def calculator():
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    performance = input("Select an action:(+,-,,/,**) ")
    if performance == "+":
        print(f'Equals:{first+second}')
    elif performance == "-":
        print(f'Equals:{first - second}')
    elif performance == "*":
        print(f'Equals:{first * second}')
    elif performance == "/":
        while True:
            try:
                first / second
            except ZeroDivisionError:
                print("You can't divide by zero")
                second = float(input("Enter the second number again: "))
                continue
            else:
                break
        print(f'Equals:{first / second}')
    elif performance == "**":
        print(f'Equals:{first ** second}')

calculator()
