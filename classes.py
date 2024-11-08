# 1.Create a class called Student with attributes name and age.
# Add a method introduce that prints: "Hello, my name is [name] and I am [age] years old."
# Create an object of Student and call the introduce method.
# 2.Define a class Calculator with methods add, subtract, multiply, and divide that perform the respective operations on two numbers.
# Create an object of Calculator and use it to perform some calculations.

#1
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"{self.name} {self.age}"

student_one=Student("Ashley",20) 
print(f"Hello my name is {student_one.name} and I am {student_one.age} years old")    


#2
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        add=self.num1+self.num2
        return add
    def sub(self):
        sub=self.num1-self.num2
        return sub
    def divide(self):
        divide=self.num1/self.num2
        return divide
    def mult(self):
        mult=self.num1*self.num2
        return mult
    
solution1=Calculator(20,30)
print(solution1.add())    
    
       
