"""Write a Python program to calculate the sum of all the elements in a list.

    Bonus points if you can make the user enter their own list"""
num = list(input("Enter the Sequence seperate by comma").split(","))
sum=0
for nums in num:
    sum+=int(nums)
print(sum)