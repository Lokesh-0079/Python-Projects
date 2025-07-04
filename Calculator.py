



def calculator():

    if operator == '+':
        return f"The addition of the two numbers is :{num1+num2:.2f}"
    elif operator == '-':
        return f"The subtraction of the two numbers is :{num1-num2:.2f}"
    elif operator == '*':
        return f"The multiplication of the two numbers is :{num1*num2:.2f}"
    elif operator == '/':
        return f"The division of the two numbers is :{num1/num2:.2f}"
    elif operator == '%':
        return f"The modulous of the two numbers is : {num1%num2:.2f}"
    else:
        return f"The {operator} is not a valid one!"

operator=input("Enter the operator:")
num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2nd number:"))

print(calculator())