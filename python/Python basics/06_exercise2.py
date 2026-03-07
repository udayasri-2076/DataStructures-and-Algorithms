import math

radius=float(input('enter the radius of a circle:'))
circumference=2*math.pi*radius
print(f"The circumference is: {round(circumference,2)}cm")

#2.Area of circle

radius=float(input("enter the radius of a circle: "))
area=math.pi*pow(radius,2)
print(f"the area of the circle is: {round(area,2)}")


import math
a=float(input("enter sideA:"))
b=float(input("enter side b:"))

c=math.sqrt(pow(a,2)+pow(b,2))
print(c)