"""
    Ask the user for a number.
    Depending on what number they enter, tell them if the number is an even or odd number.
"""
iVar1=input("Enter the No To Check Even Or Odd No-")
print(int(iVar1)%2)
if(int(iVar1)%2==0):
  print("Given Number is Even-"+iVar1)
else:
  print("Given Number is Odd-"+iVar1)