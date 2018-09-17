"""
Follow up challenge: Write a program (in a new file called LastName_challenge.py) that
will ask the user to enter in three legs of a triangle and then test to see if the triangle is: (14
points)
a. Not a triangle (a + b < c) *Test this first. If this test fails, exit the program
b. A right triangle (a2 + b2 = c2)
c. An Obtuse triangle (a2 + b2 < c2)
d. An Acute triangle (a2 + b2 > c2)
"""

print("Now if you would be so kind, please enter the lengths of a triangle:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if c > a + b:
    exit("y'all, that's not a triangle")
elif a**2 + b**2 == c**2:
    print("wow, a right triangle.")
elif a**2 + b**2 < c**2:
    print("wow, an obtuse triangle.")
elif a**2 + b**2 > c**2:
    print("wow, an acute triangle.")
       
    



