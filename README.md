# inversKinematicParallelScara
invers kinematics for parallel scara (:

This program is designed to calculate the angles required for two motors based on user-input coordinates (x and y values). The motors are part of a larger system, and these angles are necessary for positioning and controlling the system.

The program begins by taking user input for the x and y values and multiplying them by 10. These values represent the coordinates of a point in a Cartesian plane.

Next, it calculates the value of "c" using the Pythagorean theorem, which represents the distance between the origin (0,0) and the input coordinates (x, y). The program then calculates the V angle, which is the arctangent of y/x.

Using the law of cosines, the program determines the angle "Y" in radians by considering the known lengths of three sides of a triangle. The values 87.559, 90, and c represent the sides of the triangle, with the angle Y opposite the side of length 90. The calculated angle Y is then converted to degrees.

Moving to the right side of the system, the program calculates the value of "e" using the Pythagorean theorem, which represents the distance between the point (x, y) and a fixed point with coordinates (d, 0). The program then calculates the psi angle, which is the arctangent of y/(d-x).

Again, using the law of cosines, the program determines the angle "E" in radians by considering the known lengths of three sides of another triangle. The values 87.559, 90, and e represent the sides of the triangle, with the angle E opposite the side of length 90. The calculated angle E is then converted to degrees.

Finally, the program rounds the values of m1 and m2, which represent the angles for motor 1 and motor 2, respectively. These angles are calculated based on the sum of angles V and Y for motor 1, and the difference between pi and E and psi for motor 2.

The program outputs the rounded values of m1 and m2, representing the required angles for motor 1 and motor 2, respectively. These angles can be used in the larger system to control the motors and position the system accordingly.

source for math equations: https://cdn.hackaday.io/files/1733257415536800/Educational%20Five-bar%20parallel%20robot_.pdf

(ps yes i let chat gpt write this)
