"""
planet = ["jupiter", "earth", "saturn","mars","pluto"]
planet.insert(3, "neptune")
print(planet)
"""
planet = ["jupiter", "earth", "saturn","mars","pluto"]
#planet = [p.capitalize() for p in planet]
#print(planet)

for i in range (len(planet)):
    new = planet[i]
    string = new[0].upper() + new[1:]
    planet[i] = string
    print(planet)