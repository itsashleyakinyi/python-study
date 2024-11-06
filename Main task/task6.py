#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
#using while loop

# # Set the correct password and maximum attempts
# password="admin@123"
# max_attempts=4

# #initialize attempt counter
# attempts=0

# #loop until attempts reaches max attempts
# while attempts<max_attempts:
#     #prompt user for password
#     user_password=input("Enter password: ")
#     #check if password is correct
#     if user_password==password:
#         display="access granted"
#         break
#     else:
#         attempts+=1
#         print(f"incorrect password,try again;{attempts} attempts remaining")

#         #check if attempts exceeded maximum limit
# if attempts==max_attempts:
#     display="account is blocked"


# print(display)



password="admin@123"
max_attempts=4

for attempts in range(max_attempts):
    user_password=input("Enter password: ")
    if user_password==password:
        display="Access is granted"
        break 
    else:
        max_attempts-=1
        print(f"Incorrect password,try again you have {max_attempts} remaining")
        
    if max_attempts<4:
        display="Account is blocked"

print(display)


