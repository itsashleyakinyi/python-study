# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
correct_email="admin@mail.com"
correct_password="Admin@123"
max_attempts=3

for attempt in range(max_attempts):
    email=input("Enter email address: ")
    password=input("Enter password: ")
    if attempt>max_attempts:
        if correct_email==email and correct_password==password:
            display="Login is successful"
            break
        else:
            correct_email!=email or correct_password!=password
            max_attempts-=1
            print(f"Invalid username or password.Try again you have {max_attempts} attempts remaining")

        if attempt>=max_attempts:
            display="Your account is blocked"

    print(display)


