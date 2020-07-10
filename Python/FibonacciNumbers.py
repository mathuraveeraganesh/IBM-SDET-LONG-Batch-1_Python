"""Using Recursion:
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
    Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13,"""

def fibonnaci(n):
    if n<=1:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

Limit=int(input("Enter the range-"))
for x in range(Limit):
    print(fibonnaci(x))