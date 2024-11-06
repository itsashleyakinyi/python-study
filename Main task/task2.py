# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

num=int(input("Enter number: "))
ans=""
if num % 2==0:
    ans="Even"
else:
    ans="Odd"

print(f"{num} is {ans}")


if num % 4==0:
    print(f"{num} is divisible by 4")
else:
    print(f'{num}is not divisible by 4')