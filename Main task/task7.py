# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

marks=int(input("Enter marks: "))
if marks>=0 and marks<=100:
    if marks>79:
        grade="A"
    elif marks<=79 and marks>=60:
        grade="B"
    elif marks<=59 and marks>=49:
        grade="C"
    elif marks<49 and marks>=40:
        grade="D"
    else:
        grade="E"
else:
    grade="Invalid marks"
print(grade)   

