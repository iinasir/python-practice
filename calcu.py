first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operations = input("Enter the operation (+, -, *, /): ")
if operations == "+":
    print(f"Result: {first + second}")
elif operations == "-":
    print(f"Result: {first - second}")
elif operations == "*":
    print(f"Result: {first * second}")
elif operations == "/":
    if float(second) == 0:
        print("Error : Cant devide by zero")
    else:
        print(f"Result: {float(first) / float(second)}")
else:
    print("Invalid operation!")
