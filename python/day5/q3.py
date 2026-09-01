#Q3 — Find Smallest
#Don't use: min()
numbers=[20, 50, 10, 40]
smallest=numbers[0]

for i in numbers:
    if i<smallest:
        smallest=i

print("Smallest=",smallest)
