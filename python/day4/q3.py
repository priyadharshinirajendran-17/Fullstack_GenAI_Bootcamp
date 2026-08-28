def find_largest(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

result= find_largest(20, 40, 10)
print("Largest=", result)