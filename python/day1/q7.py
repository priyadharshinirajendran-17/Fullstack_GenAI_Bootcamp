number=[]
for i in range(5):
    value=int(input(f"Enter number {i+1}:"))
    number.append(value)

largest=number[0]
for n in number:
    if n > largest:
        largest=n

print("Largest number:", largest)