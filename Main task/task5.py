# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
num3=int(input("Enter num 3: "))

if num1>num2 and num1>num3:
    display=f"{num1} is largest"
elif num2>num1 and num2>num2:
    display=f"{num2} is largest"
else:
    display=f"{num3} is largest"  

print(display)