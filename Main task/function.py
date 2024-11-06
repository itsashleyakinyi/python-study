# function to create area of a triangle:
def triangle_area():
    base=10
    height=15
    area=base*height*0.5
    return area
triangle_area()  

#create a function that calculate the area of a rectangle
def calculate_area():
    length=100
    width=50
    area=length * width
    return area
calculate_area()

def calc_tri_area(base,height):
    area=0.5 * base * height
    return area
area_1=calc_tri_area(10,15) 
area_2=calc_tri_area(20,40)  
print(area_1,area_2)

#create a function that checks whether a number is odd or even.(store the called functions in a variable)
def odd_or_even(num):
    if num % 2==0:
        display=f"{num} is even"
    else:
        display=f"{num} is odd"
    return display
user_1=int(input("Enter number: "))
user_2=int(input("Enter number: "))
x=odd_or_even(user_1)
y=odd_or_even(user_2)
print(x)
print(y)