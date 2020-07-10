"""Write a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old"""
sName=input("Enter Your name-")
iAge=input("Enter Your Age-")
var1=100-int(iAge)
var2=var1+2020
var3=sName+" will turn 100 years old in-{}"
print(var3.format(var2))