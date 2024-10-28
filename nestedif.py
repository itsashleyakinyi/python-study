# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
account=input("enter account type standard/premium: ")
ts=float(input("enter amount: "))
if account=="standard":
    if ts>500:
        print("Transaction exceeds the limit for standard accounts")
    else:
        print("Transaction approved")
elif account=="Premium":
    if ts>1000:
        print("Transaction exceeds the limit for premium accounts")
    else:
        print("transaction approved")
else:
    print("invalid account type Please enter either'standard' or 'premium' ")
