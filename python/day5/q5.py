#Q5 — Separate Even and Odd Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#Produce:
#Even: [2, 4, 6, 8]
#Odd: [1, 3, 5, 7]

numbers=[1, 2, 3, 4, 5, 6, 7, 8]
even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even List:",even)
print("Odd List:",odd)
