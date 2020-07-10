"""Write a function sum() such that it can accept 
a list of elements and print the sum of all elements"""

def sum(add):
    num=0
    for x in add:
        num+=int(x)
    return(num)

list1=[1,2,3,4]
result=sum(list1)
print("Sum of the All Element-"+str(result))

