#Goal is to ask the user of their name and format it accordingly


import re

name= input("Whats your name? ").strip()

if matches := re.search("^(.+), *(.+)$",name):
    name = matches.group(2)+" "+ matches.group(1)

print(f"hello,{name}")    