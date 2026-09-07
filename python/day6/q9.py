#Swap two variables.Using tuple unpacking, swap: a=10, b=20. don't use a third variable.

numbers=(10, 20)
a,b=numbers
a,b=b,a
print("After swapping a:",a)
print("After swapping b:",b)