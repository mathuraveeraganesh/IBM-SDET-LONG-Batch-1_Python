"""Write a Python program to create the multiplication table (from 1 to 10) of a number."""
num=input("Enter the Number to Create Multiplication Table-")
for x in range(1,11):
    value=x*int(num)
    value2="{}*"+num+"={}"
    print(value2.format(x,value))
    
