def fnc_teste1():
    print("iniciando, estrutura da fnc")

fnc_teste1()

#atribuindo retorno da fnc em output
output = fnc_teste1()


#retorna implicitamente None qd não retorna nada
print(output) 

output


#fnc com retorno
def rocket_parts():
    return "payload, propellant, structure"

output2 = rocket_parts()
print(output2) 
output2
print(output2) 


# retorna true apenas se tiver um true

print( any([True, False, False]) )

print( any([False, False, False]) )

# exige argumento
print( any([False]))
#any()


print( str() )
print( str(15) )
print( str(15454151515151) )

#exigindo argumento entre ()

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
TESTE = distance_from_earth("Moon") 
print(TESTE)
print( distance_from_earth("Moon") )
print( distance_from_earth("MooDDn") )
distance_from_earth("Moon")

# mais que um argumento

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print( days_to_complete(238855, 75) )

# passando fnc como argumento
total_days = days_to_complete(238855, 75)
round(total_days)

round(days_to_complete(238855, 75))



# timedelta permite a soma das horas 

from datetime import timedelta, datetime


def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

def tempo(horas=51):
    agora = datetime.now()
    final = agora + timedelta(hours=horas)
    return final.strftime("FINAL: %A %H:#M ") 

print(tempo())

print(tempo(horas=0))



#obrigatorio argumento destination
from datetime import timedelta, datetime

def arrival_time2(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")



# erro arrival_time2()
print(arrival_time2("Moon"))

print(arrival_time2("Orbit", hours=0.13))



# Quantidade variável de argumentos

def tamanho_argumentos(*args):
    print(args)

def variable_length(*args):
    print(args)

variable_length()
variable_length("one", "two")
variable_length(None)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

sequence_time(4, 14, 18)


def tempo_lancamento(*args):
    total = sum(args)

    if total < 60:
        return f"Falta {total} minutos para o lançamento"
    else:
        return f"Falta {total/60} hours"


print(tempo_lancamento(5,10,5))

print(tempo_lancamento(3,6,9))

#quantidade de argumentos palavras chaves

def variable_length(**kwargs):
    print(kwargs)


variable_length(tanks=1, day="Wednesday", pilots=3)

def tripulacao(**kwargs):
    print(f"len{kwargs} astronautas na missão")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")



tripulacao(aptain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")



def fuel_tanks(**args):
    for name, value in args.items():
        print(f'{name}: {value}')

fuel_tanks(main = 50, external = 100,emergency = 60)