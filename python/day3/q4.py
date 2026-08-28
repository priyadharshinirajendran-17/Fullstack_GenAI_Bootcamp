# Problem 4 — Count Digits Input: 123456 Output:6
 
number=int(input("Enter the number:"))
count=0
while number>0:
    number//=10
    count+=1
print("Number of digits=",count)