#Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))
# num3=int(input("Enter number 3: "))
# num4=int(input("Enter number 4: "))
# largest=max(num1,num2,num3,num4)
# print(f"{largest} is largest")


def largest_number(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        display=f"{num1} is largest"
    elif num2>num1 and num2>num3 and num2>num4:
        display=f"{num2} is largest"
    elif  num3>num1 and num3>num2 and num3>num4:
        display=f"{num3} is largest"
    else:
        display=f"{num4} is largest"
    return display
input_1=int(input("Enter number 1: "))
input_2=int(input("Enter number 2: ")) 
input_3=int(input("Enter number 3: "))  
input_4=int(input("Enter number 4: "))
a=largest_number(input_1,input_2,input_3,input_4) 
print(a)    