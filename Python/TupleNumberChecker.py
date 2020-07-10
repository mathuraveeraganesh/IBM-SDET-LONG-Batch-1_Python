"""
Given a tuple of numbers, iterate through it and print 
only those numbers which are divisible by 5
Bonus points if you can make the user enter their own tuple.
"""
#tuple1=(1,10,3,20,30,8)
tuple1=tuple(input("Enter the value").split(","))
for x in tuple1:
    if int(x)%5==0:
        print(x)