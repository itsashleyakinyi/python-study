# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

num1=int(input())
num2=int(input())
num3=int(input())

if num1>num2 and num1>num3:
    print("Num1 is largest")
elif num2>num1 and num2>num3:
    print("Num2 is largest")
else:
    print("Num3 is largest")


temp1=int(input())
if temp1>30:
        print("The temperature is too high")
elif temp1>15 and temp1<30:
        print("Normal Temperature")
else:
        print("Cold temperature")

x=int(input())
y=int(input())
if x>10 and x<20 and y>100:
            print("Conditions met")
else:
            print("Conditions not met")

password=input()
if password=="Secret123":
        print("Access is granted")
else:
        print("Access is denied")

student_score=int(input("Enter student score: "))
attendance=int(input("enter student attendance:gi "))
if student_score > 90:
        if attendance > 80:
            print("Excellent student")
        else:
            print("Good score, but attendance needs improvement")
else:
        print("Score does not meet the threshold for evaluation")
        
