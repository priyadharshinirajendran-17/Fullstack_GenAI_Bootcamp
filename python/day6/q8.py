#Find Index. Given- numbers=(10, 20, 30, 40, 50)
#Find the index of 40. Expected output: Index: 3.

numbers=(10, 20, 30, 40, 50)
target=40
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Index:",i)
        break