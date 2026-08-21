#Grade Calculator

mark=int(input("Enter the mark="))
if mark>=90 and mark<=100:
    print("A grade.")
elif mark>=80 and mark<90:
    print("B grade.")
elif mark>=70 and mark<80:
    print("C grade.")
elif mark>=60 and mark<70:
    print("D grade.")
elif mark>=0 and mark<60:
    print("F grade.")
else:
    print("Please enter valid mark")