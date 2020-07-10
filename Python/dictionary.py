"""
Create a Python dictionary that contains a bunch of fruits
 and their prices.
Write a program that checks if a certain fruit is available or not.
"""
check=input("Enter the Fruit Name:")
dict1={"Apple":240,"Orange":160,"Banana":200}
for fruit in dict1:
    if fruit==check:
        value=check+" Available and the Price {}"
        print(value.format(dict1[fruit]))
        raise SystemExit
        
else:
    print(check+" is not Available")
    raise SystemExit