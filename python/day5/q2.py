#Q2 — Find Largest Given a list, find the largest value. 
# Don't use: max()

numbers=[10, 20, 30, 40]
largest=numbers[0]

for i in numbers:
    if i>largest:
        largest=i

print("Largest=")