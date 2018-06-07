# import complex math module
import cmath

# general quadratic equation is ax**2 + bx + c

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("And Enter the value of c: "))

# printing the full equation
print('The Quadratic Equation is ',a,'x**2 + ',b,'x + ',c,sep='')

# calculating discriminant
d = (b**2) - (4*a*c)

# evaluating first root
r1 = (-b + cmath.sqrt(d)) / (2*a)
r2 = (-b - cmath.sqrt(d)) / (2*a)

# prinring the roots
print("First root:",r1)
print("Second root:",r2)