first = input("Enter the first number: ")
second = input("Enter the second number: ")
operations = input("Enter the operation (+, -, *, /): ")

if operations == "+":
    print(f"Result: {float(first) + float(second)}")
elif operations == "-":
    print(f"Result: {float(first) - float(second)}")
elif operations == "*":
    print(f"Result: {float(first) * float(second)}")
elif operations == "/":
    print(f"Result: {float(first) / float(second)}")
else:
    print("Invalid operation!")

    