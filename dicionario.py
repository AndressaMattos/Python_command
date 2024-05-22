planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name') )


print(planet['name'])


wibble = planet.get('wibble') # Returns None
#wibble = planet['teste'] # Throws KeyError


planet.update({'name': 'Makemake'})
planet.update({'moons': 2})

#update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

planet['name'] = 'Jupiter'
planet['moons'] = 79

#adicionar atributo
planet['orbital period'] = 4333

#remover atributo
planet.pop('orbital period')




# Um dicionario pode armazenar  um dicionario 
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(planet.get('diameter (km)'))

print(planet['diameter (km)'])

print(f'Planeta {planet.get("name")}') #adicionando o f antes das aspas é possível chamar ver no texto com {}


print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')



# Enter code below

planet['moons'] = 1

planet.update({
    'name' : 'Earth'
    })

planet['circunference (km)'] = {
    'polar' : 6752,
    'equatorial': 6792
}


print(f'{planet.get("name")} has {planet["moons"]} moon(s) \b and of  {planet["circunference (km)"]} sendo {planet["circunference (km)"]["polar"]}')


# imprimir todas os atributos do planet
for key in planet.keys() :
    print(f'{key}: {planet.get("moons")}')



rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
    
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')



# Se dezembro existir,  adiciona 1 no valor, saindo de 2.1 para 3,1
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Se não, cria


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

luas = planet_moons.values()

print(luas)

total_planetas = len(planet_moons.keys())

print(total_planetas)
print(len(planet_moons.keys()))
print(len(planet_moons))


total_luas = 0

for moon in luas:
    total_luas = total_luas + moon


average =  total_luas / total_planetas


print(f'Each planet has an average of {average} moons')