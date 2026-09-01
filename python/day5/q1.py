# Q1 — Create a List Take 5 numbers from the user and store them in a list.
#Example- Input:
#10
#20
#30
#40
#50
#Output: [10, 20, 30, 40, 50]

numbers=[]
n=int(input("Enter number of values:"))
for i in range(0,n):
    value=int(input(f"Enter num {i+1}:"))
    numbers.append(value)
print("List=",numbers)