from math import pi #Import pi only from math module#
radius = float(input("Enter the radius: "))
volume = (4/3) * pi * pow(radius, 3)
print("The volume of sphere is",str(round(volume,2)), "m")