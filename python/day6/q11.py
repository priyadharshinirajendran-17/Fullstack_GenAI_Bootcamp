#Find the smallest in Tuple.
#find the smallest number without using min().

numbers=(10, 45, 23, 67, 12)
smallest=numbers[0]
for n in numbers:
    if n<smallest:
        smallest=n
print("Smallest number:", smallest)