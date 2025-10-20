def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    
    try:
        result = num / den
        print("The result of the divison is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")