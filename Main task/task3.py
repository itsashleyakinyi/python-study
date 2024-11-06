# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”


phone_num=input("Enter number: ").strip()
if phone_num.startswith("+254") and len(phone_num)==13:
     display=phone_num 
elif phone_num.startswith("07") and len(phone_num)==10:
     display='+254' + phone_num.lstrip("0")
elif phone_num.startswith("7") and len(phone_num)==9:
     display="+254" + phone_num
elif phone_num.startswith("254") and len(phone_num)==12:
     display="+" + phone_num
elif phone_num.startswith("01") and len(phone_num)==10:
     display="+254" + phone_num.lstrip("0")
elif phone_num.startswith("1") and len(phone_num)==9:
     display="+254" + phone_num
else:
     display="Invalid phone number."
print(display)         

