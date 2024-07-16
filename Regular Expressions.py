#Goal is to prompt a user for there email and check if it matches the conventional syntax 


import re

email = input("Whats your email?").strip()

if re.search(r"^\w+@\w+\.(edu|com|org)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")    