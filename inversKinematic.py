import numpy as np
import math


x = float(input("enter x value in cm: ")) * 10
y = float(input("enter y value in cm: ")) * 10
info  = str(input("show more info ? y/n: "))

d = 105
farm = 90
sarm = 87.559

#left side

#calculate c
c = math.sqrt(x**2 + y**2)

#calculate v angel
V = math.atan(y/x)

#calculate angel Y in radiants
Y = math.acos((0 - sarm**2 + farm**2 + c**2) / (2 * farm * c))

m1 = V + Y
m1 = np.rad2deg(m1)


#right side

#calculate e
e = math.sqrt((d-x)**2 + y**2)

#calculate the angel psi in radians
psi = math.atan(y / (d - x))

#calculate the angel E in radiants
E = math.acos((0 - sarm**2 + farm**2 + e**2) / (2 * farm * e))

m2 = math.pi - E - psi
m2 = np.rad2deg(m2)


#round the numbers
m1r = round(m1)
m2r = round(m2)

if info == "y":
    print("m2: " + str(m2))
    print("E: " + str(E))
    print("psi: " + str(psi))
    print("e: " + str(e))
    print("m1:" + str(m1))
    print("Y: " + str(Y))
    print("v: " + str(V))
    print("c:" + str(c))

print("The angel for motor 1 is: " + str(m1r))
print("The angel for motor 2 is: " + str(m2r))
