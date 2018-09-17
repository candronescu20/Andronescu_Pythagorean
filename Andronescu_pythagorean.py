
name=raw_input("Hello, what is your name? ")

print("Nice to meet you, " + name+".")

from math import sqrt
print("Now if you would be so kind, please enter the lengths of the shorter sides of a right triangle:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt((a**2) + (b**2))
print("Given those numbers, " + str(a) + " and " + str(b) + ", the length of the hypotenuse would be " + str(c))
