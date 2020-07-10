"""
Given a list of numbers, return True if first and last number of a list is same.
    Bonus points if you can make the user enter their own list.
"""
number=list(input("Enter the list of Number").split(","))
if number[0]==number[-1]:
    print("True")
else:
    print("False")