def basic_calculator(a, b, operation):
    if a.isnumeric() & b.isnumeric():
        a = float(a)
        b = float(b)
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "divide":
            if b != 0:
                result = a / b
            else:
                result = "Cannot divide by 0, please provide a valid number"
        elif operation == "multiply":
            result = a * b
        else:
            result = "Operations supported: add, subtract, divide, multiple only"

    else:
        result = "Please enter a valid number for a & b"

    return result
