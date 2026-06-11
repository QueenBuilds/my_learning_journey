password=input("Entre the password:")
digit=False
uppercase=False
size=len(password)
for cha in password:
    if cha.isdigit():
        digit=True
    if cha.isupper():
        uppercase=True

if size>=8 and digit and uppercase:
    print("Strong password")
else:
    print("Weak password")