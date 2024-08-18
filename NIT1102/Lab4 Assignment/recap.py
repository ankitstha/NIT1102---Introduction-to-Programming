from math import pi
radius = int(input("Enter the radius of the circle: "))
print("%15s%15s" % ("Radius  (m)", "Volume (m\u00b3)"))
# print the volume of the sphere 10 times with increment of 1 along with the radius
for i in range(10):
    volume = 4/3 * pi * radius**3
    print("%15d%15.2f" % (radius,volume))
    volume = volume + 1
    radius = radius + 1
