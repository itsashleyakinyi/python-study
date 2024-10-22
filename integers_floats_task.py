#Questions
#1.Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
#2.Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
#3.Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
#4.Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 



temp=56.8926
temp=round(temp,)
print(temp)


temp2=56.8926
temp2=round(temp2,2)
print(temp2)

temp3=56.8926
temp3=round(temp3,3)
print(temp3)


temp4=56.8926
temp4=str(temp4)
print(temp4)

temp5=temp4[3:7]
print(temp5)

temp5="8926"
temp6="8"+"."+"926"
print(temp6)

temp6="8.926"
temp=float(temp6)
print(temp6)
