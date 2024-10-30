# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.



# Task 1: Display numbers from 1 to 50 in a list
numbers = list(range(1, 51))
print("Numbers from 1 to 50:", numbers)

# Task 2: Display numbers divisible by 7 or 5 inside a list
divisible_by_7_or_5 = [num for num in numbers if num % 7 == 0 or num % 5 == 0]
print("Numbers divisible by 7 or 5:", divisible_by_7_or_5)




#method2
# divisible_by_7_or_5=[]
# for num in numbers:
#     if num % 7 == 0 or num % 5 == 0:
#         divisible_by_7_or_5.append(num)
# print(divisible_by_7_or_5)        

# Task 3: Find the sum and average of values between 10 and 40
range_10_to_40 = list(range(10, 41))
sum_range = sum(range_10_to_40)
average_range = sum_range / len(range_10_to_40)
print("Sum of numbers from 10 to 40:", sum_range)
print("Average of numbers from 10 to 40:", average_range)

#Method2
# sum=0
# count=0
# for i in range_10_to_40:
#     sum+=i
#     count+=1
# print(sum)
# average=sum/count
# print(average)

# Task 4: Put the first 10 odd numbers between 10 and 50 into a list
odd_numbers = [num for num in range(10, 51) if num % 2 != 0][:10]
print("First 10 odd numbers between 10 and 50:", odd_numbers)
#method2
# num=list(range(11,50,2))
# odd=[]
# for x in num:
#     odd.append(x)
#     if len(odd==10):
#         break

# method3
# for x in num:
#   if x % 2 !=10:
#     odd.append(x)
#     count+=1
#     if count==10:
#       break
         


# Task 5: Program to take a number input and print its multiplication table up to 10
number = int(input("Enter a number to get its multiplication table up to 10: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Task 6: Program to count and print the number of even numbers between 1 and 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("Number of even numbers between 1 and 50:", len(even_numbers))

#Method2
# for i in range(1,51):
#     if i % 2==0:
#        count+=1

# print(count)
# Task 7: Total quantity of ls1
ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]
total_quantity = sum(quantity for name, quantity in ls1)
print("Total quantity in ls1:", total_quantity)



#method2
# t_quantity=0
# for l in ls1:
#     stock=l[1]
#     t_quantity+=stock
#     print(t_quantity)  