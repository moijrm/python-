def addition(a,b):
    return a + b
def soustraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b

result = 0
history = []

print("===CALCULATOR===")
while True:
    try:
        first = int(input("Enter the first number : "))
    except ValueError:
        print("Invalid value")
        continue
   
    operator = input("Enter an operator (+,-,*,/) : ")
   
    if operator not in["+","-","*","/"]:
        print("Invalide operator")
        continue
       
   
    try:
        second = int(input("Enter the second number : "))
    except ValueError:
        print("Invalid value")
        continue
    if operator == "+":
        result = addition(first,second)
        print(result)  
    elif operator == "-":
        result = soustraction(first,second)
        print(result)   
    elif operator == "*":
        result = multiplication(first,second)
        print(result)       
    elif operator == "/":
        try:
            result = division(first,second)
        except ZeroDivisionError:
            print("Cannot division by Zero")
            continue
        print(result)
    else : 
        print("Invalid operator")
        continue
    
    history.append(f"{first} {operator} {second} = {result}")
    
    next = input("Continue (yes, no)? : ")
    if next in ["no","n"]:
        for history in history:
            print(history)
        break