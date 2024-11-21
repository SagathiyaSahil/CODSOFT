import math

# Basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def floor_divide(x, y):
    return x // y

# Trigonometric functions
def sine(x):
    return math.sin(math.radians(x))  # Convert degrees to radians

def cosine(x):
    return math.cos(math.radians(x))  # Convert degrees to radians

def tangent(x):
    return math.tan(math.radians(x))  # Convert degrees to radians

def inverse_sine(x):
    return math.degrees(math.asin(x))  # Convert radians to degrees

def inverse_cosine(x):
    return math.degrees(math.acos(x))  # Convert radians to degrees

def inverse_tangent(x):
    return math.degrees(math.atan(x))  # Convert radians to degrees

# Advanced math functions
def square_root(x):
    if x < 0:
        return "Error! Negative number cannot have a real square root."
    return math.sqrt(x)

def natural_logarithm(x):
    if x <= 0:
        return "Error! Logarithm is undefined for zero or negative values."
    return math.log(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error! Invalid input for logarithm."
    return math.log(x, base)

def factorial(x):
    if x < 0 or not x.is_integer():
        return "Error! Factorial is only defined for non-negative integers."
    return math.factorial(int(x))

def permutation(n, r):
    if n < 0 or r < 0 or n < r:
        return "Error! Invalid input for permutation."
    return math.perm(n, r)

def combination(n, r):
    if n < 0 or r < 0 or n < r:
        return "Error! Invalid input for combination."
    return math.comb(n, r)

def exp(x):
    return math.exp(x)

# Hyperbolic functions
def sinh(x):
    return math.sinh(math.radians(x))

def cosh(x):
    return math.cosh(math.radians(x))

def tanh(x):
    return math.tanh(math.radians(x))

# Main program
def calculator():
    print("Advanced Python Calculator with Trigonometry and Advanced Math Functions")

    while True:
        try:
            # Taking user input for the first number, second number, and operation choice
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            print("\nSelect operation:")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. Modulus (%)")
            print("6. Exponentiation (^)")
            print("7. Floor Division (//)")
            print("8. Sine (sin) of first number")
            print("9. Cosine (cos) of first number")
            print("10. Tangent (tan) of first number")
            print("11. Inverse Sine (asin) of first number")
            print("12. Inverse Cosine (acos) of first number")
            print("13. Inverse Tangent (atan) of first number")
            print("14. Square Root (√) of first number")
            print("15. Natural Logarithm (ln) of first number")
            print("16. Logarithm (log) of first number to a given base")
            print("17. Factorial of first number")
            print("18. Permutation (nPr) of first and second number")
            print("19. Combination (nCr) of first and second number")
            print("20. Exponential function (e^x) of first number")
            print("21. Hyperbolic Sine (sinh) of first number")
            print("22. Hyperbolic Cosine (cosh) of first number")
            print("23. Hyperbolic Tangent (tanh) of first number")
            print("24. Exit")

            operation = input("Enter operation (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24): ")

            if operation == '1':
                print(f"The result is: {add(num1, num2)}")
            elif operation == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif operation == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif operation == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif operation == '5':
                print(f"The result is: {modulus(num1, num2)}")
            elif operation == '6':
                print(f"The result is: {exponentiate(num1, num2)}")
            elif operation == '7':
                print(f"The result is: {floor_divide(num1, num2)}")
            elif operation == '8':
                print(f"The sine of {num1} degrees is: {sine(num1)}")
            elif operation == '9':
                print(f"The cosine of {num1} degrees is: {cosine(num1)}")
            elif operation == '10':
                print(f"The tangent of {num1} degrees is: {tangent(num1)}")
            elif operation == '11':
                print(f"The inverse sine (asin) of {num1} is: {inverse_sine(num1)} degrees")
            elif operation == '12':
                print(f"The inverse cosine (acos) of {num1} is: {inverse_cosine(num1)} degrees")
            elif operation == '13':
                print(f"The inverse tangent (atan) of {num1} is: {inverse_tangent(num1)} degrees")
            elif operation == '14':
                print(f"The square root of {num1} is: {square_root(num1)}")
            elif operation == '15':
                print(f"The natural logarithm (ln) of {num1} is: {natural_logarithm(num1)}")
            elif operation == '16':
                base = float(input("Enter the base for logarithm: "))
                print(f"The logarithm of {num1} to base {base} is: {logarithm(num1, base)}")
            elif operation == '17':
                print(f"The factorial of {num1} is: {factorial(num1)}")
            elif operation == '18':
                print(f"The permutation (nPr) of {num1} and {num2} is: {permutation(num1, num2)}")
            elif operation == '19':
                print(f"The combination (nCr) of {num1} and {num2} is: {combination(num1, num2)}")
            elif operation == '20':
                print(f"The exponential (e^x) of {num1} is: {exp(num1)}")
            elif operation == '21':
                print(f"The hyperbolic sine (sinh) of {num1} degrees is: {sinh(num1)}")
            elif operation == '22':
                print(f"The hyperbolic cosine (cosh) of {num1} degrees is: {cosh(num1)}")
            elif operation == '23':
                print(f"The hyperbolic tangent (tanh) of {num1} degrees is: {tanh(num1)}")
            elif operation == '24':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid input! Please select a valid operation.")
        except ValueError:
            print("Invalid number input! Please enter valid numbers.")

# Run the calculator
calculator()
