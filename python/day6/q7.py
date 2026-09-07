#Count an element. Given: numbers=(1,2,2,3,2,4,5)

numbers=(1, 2, 2, 3, 2, 4, 5)
count=0
for num in numbers:
    if num ==2:
        count+=1
print("Count of 2:", count)