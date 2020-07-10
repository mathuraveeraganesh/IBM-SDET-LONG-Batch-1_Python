"""Write a Python program that throws a NameError.
Handle the error so it doesn't halt execution."""

try:
    print(value)
except NameError:
    print("Name is Not defined")