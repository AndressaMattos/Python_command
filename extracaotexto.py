extracao = "Mars Average Temperature: -60 C"

partes = extracao.split(':')

print(partes)
print(partes[0])
print(partes[-1])

print(' '.join(partes))



mars_temperature = "aqui The highest temperature on Mars1 2 is about 30 C"

for item in mars_temperature.split():
    if item.isnumeric():
        print(item)




if "30 C".endswith("C"):
    print ("This temperature is in Celsius")


print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))



text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())



moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))