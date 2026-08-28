#Problem 3 — Multiplication Table Input: 7 Output: 7 x 1 = 7 ... 7 x 10 = 70

n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",i*n)