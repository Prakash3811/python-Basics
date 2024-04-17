num1=int(input())
num2=int(input())
operator=input()

if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1//num2)
else:
    print("Invalid operator")
