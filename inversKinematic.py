import numpy as np
import math


x = float(input("enter x value: ")) * 10
y = float(input("enter y value: ")) * 10

d = 105
farm = 90
sarm = 87.559

#left side

#calculate c
c = math.sqrt(x**2 + y**2)
print("c:" + str(c))

#calculate v angel

V = math.atan(y/x)
print("v: " + str(V))

#calculate angel Y in radiants

Y = math.acos((0 - 87.559**2 + 90**2 + c**2) / (2 * 90 * c))
print("Y: " + str(Y))

m1 = V + Y
m1 = np.rad2deg(m1)
print("m1:" + str(m1))

#right side

#calculate e
e = math.sqrt((d-x)**2 + y**2)
print("e: " + str(e))

#calculate the angel psi in radians
psi = math.atan(y / (d - x))
print("psi: " + str(psi))

#calculate the angel E in radiants
E = math.acos((0 - 87.559**2 + 90**2 + e**2) / (2 * 90 * e))
print("E: " + str(E))

m2 = math.pi - E - psi
m2 = np.rad2deg(m2)
print("m2: " + str(m2))

#round the numbers
m1r = round(m1)
m2r = round(m2)

print("The angel for motor 1 is: " + str(m1r))
print("The angel for motor 2 is: " + str(m2r))
