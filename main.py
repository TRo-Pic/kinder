a = int(input("Ввдетие А: "))
b = int(input("Ввдетие B: "))
operation = input("Введите знак операции: ")
#/ // % * - +
if operation == "+":
    print(f"A {operation} B = {a + b}")
elif operation == "-":
    print(f"A {operation} B = {a - b}")
elif operation == "*":
    print(f"A {operation} B = {a * b}")
elif operation == "/":
    print(f"A {operation} B = {a / b}")
elif operation == "%":
    print(f"A {operation} B = {a % b}")
