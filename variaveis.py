
print ("Print de variavel: ")

sum = (1+2)
print( sum )

product = sum * 2

print (product)

print("Tipos de variáveis em python:")
print("Númerico, temos int, float e complex")
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears

print("Cadeia de caracteres, temos o string str = a literal string")
on_the_moon = "Apollo 11" #string 

print("Booleanos: true e false")
teste = True


print("Também é possíel definir o tipo da variavel:")

print("type(distance_to_alpha_centauri) ## <class 'float'>")

type(distance_to_alpha_centauri) ## <class 'float'>


type(teste)



from datetime import date

print(date.today())


print("hoje é dia: "+ str(date.today()))



parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")




mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)


print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))


mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))


mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

print(round(100/6, 1))

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")


subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)