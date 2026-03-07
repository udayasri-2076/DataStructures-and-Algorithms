#Exercise 1 Rectangle Area Calc

length=int(input("enter the length: "))
width=int(input("enter the width:"))
area=length*width
print(f"the area of rectangle is: {area}cm")  

'''
Output
enter the length: 12
enter the width:4
the area of rectangle is: 48cm
'''

#Exercise 2:Shoppiing cart program

item=input("what items u like to buy?:")
price=float(input("what is the price?:"))
quantity=int(input("how many would u like?:"))
total=price*quantity

print(f"you have bought {quantity}X{item}/s")
print(f"your total is: ${total}")