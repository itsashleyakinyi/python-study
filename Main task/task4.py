# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email_address=input("Enter email address: ")

if "@" and "." in email_address:
    display=f"{email_address} is valid"
else:
    display=f"{email_address} is invalid" 
print(display)       
