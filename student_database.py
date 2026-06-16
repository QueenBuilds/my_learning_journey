student_name={}
count=1
while True:
    name=input("entre the name=")
   
    if name=="exit":
        break
    if name not in student_name.values():
        student_name[count]=name
        count+=1
    
   
    print(student_name)
print(f"total students={len(student_name)}")