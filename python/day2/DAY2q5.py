#Age category

age=int(input("Enter Your age:"))
if age>0 and age<=12:
    print("Child")
elif age>=13 and age<=17:
    print("Teenager")
elif age>=18 and age<=59:
    print("Adult")
elif age>=60:
    print("Senior citizen")
else:
    print("Negavite value not applicable")