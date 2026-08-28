#Problem 5 — Reverse a Number Input:12345 Output:54321

n=int(input("Enter the number to be reversed:"))
reverse=0
while n>0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)