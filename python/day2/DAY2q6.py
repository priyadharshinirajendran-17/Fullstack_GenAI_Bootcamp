#EB bill calculator

unit=float(input("Enter the number of units:"))
if unit>0 and unit<=100:
    cost=unit*2
    print("Cost=",cost)
elif unit>100 and unit<=200:
    cost=unit*3
    print("Cost=",cost)
elif unit>=300:
    cost=unit*5
    print("Cost=",cost)
else:
    print("Enter valid unit")