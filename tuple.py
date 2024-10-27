#create a tuple

marks=(100,300,250,160,450,600)
print(type(marks))
print(marks[5])
#converting to a list
marks=list(marks)
print(type(marks))
#converting back to a tuple
marks=tuple(marks)
print(type(marks))


days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
#2. Using a function a find the length of the tuple.
#3. Replace Thursday with Thur


print(days[2])
print(len(days))
days=list(days)
print(days)
days[3]="Thur"
print(days)
days=tuple(days)
print(days)