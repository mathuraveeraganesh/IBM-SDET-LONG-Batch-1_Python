"""Given a two list of numbers create a new list
 such that new list should contain only odd numbers 
 from the first list and even numbers from the second list."""
list1=[1,2,3,4,5,6]
list2=[11,12,13,14,15,16]
list3=[]
for num in list1:
    if not int(num)%2==0:
        list3.append(num)

for num1 in list2:
    if int(num1)%2==0:
        list3.append(num1)
print(list3)
