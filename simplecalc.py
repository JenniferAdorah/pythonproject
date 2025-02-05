num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operator=input("enter an operator (+,-,*,/: ")

# perform the calculation based on the operator

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    if num2 !=0:
        result = num1/num2
    else:
        result = "Error! Division by zero"
else:
    result = "invalid operator"
print(f"The result is : {result}")
