Name=input("entre the student name=")
Marks=int(input("entre the marks="))
print(f"Student:{Name}")
if Marks<0 and Marks>100:
    print("Invalid Marks")
else:
     
 if Marks>=90:
    print("Grade=A")
 elif Marks>=75:
    print("Grade=B")
 elif Marks>=60:
    print("Grade=C")
 else :
    print("Grade=D")

 if Marks>=40:
    print("Result=Pass")
 else:
    print("Result=Fail")

