planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print ("First planet name ",planets[0])

planets[0] =  "New name: red planet"

print ("First planet name ",planets[0])

planets[0] =  "Mercury"

planets.append("Pluto") # adicionar no final da lista

number_of_planets = len(planets) #count

print ("Ther ar actually",number_of_planets, "planets in the system solar" )

planets.pop() # retirar ultimo planeta da lista

number_of_planets = len(planets) #count

print ("Ther ar actually",number_of_planets, "planets in the system solar" )


print("The last planet is", planets[-1]) #ultimo item da fila em vez do primeiro


jupiter_index = planets.index("Jupiter") # trabalhando com index, posição
print("Jupiter is the", jupiter_index + 1, "planet from the sun")



#--------------------------------------------------------------------------------
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N") # trabalhando com minimo e máximo da list 
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

#-----------------------------------------------------------------------------------

# criando novas listas através de indices de lista

planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planetas_before_earth = planets[0:2] #ultimo não aparece earth
print(planetas_before_earth)

planets_after_earth = planets[3:8] # ultimo não aparece, tem que colocar um a mais
print(planets_after_earth) 

#----------------------------------------------------------------------------
#Unindo duas listas

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


# invertendo ordem (alfabetica)
#sort altera list
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


#sort normal organiza em ordem alfabetica
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
