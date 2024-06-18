num1=int(input("enter num 1"))
num2=int(input("enter num 2"))
operator=(input("enter a operator from +,-,*,/"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero!")
        result = None
    else:
        result = num1 / num2
else:
    print("Error: Invalid operator!")
    result = None

if result is not None:
    print("The result of ",num1,operator,num2," is:",result)
