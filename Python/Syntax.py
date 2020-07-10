variable="string"
print(variable)

numbers=23
num1=1.5
num3=1j
print(type(numbers))
print(type(num1))
print(type(num3))

#multiple print
a="""i am tester
in selenium
with java"""
print(a)

b="Hello,world"
print(b[1])
print(b[2:5])     #Slicing Strings(2,3,4)
print(len(b))
print(a.lower())
print(b.upper())
print(b.replace("l","z"))
print(b.split(","))
x="Hello" in b
y="world" not in b
print(x)
print(y)
print(a+b)   # combine Two string

c=356
d=12
e="the price {} and the ID {}"
print(e.format(c,d))
f="the Id {1} and the Price {0}"
print(f.format(c,d))

int1=int(2.8)
float1=float(3.8)
string1=str("3.8")
print(int1)
print(float1)
print(string1)
print(2**3)   #exponement 2 power of 3
print(9/2)
print(9//2)
for x in range(8):
  print(x)