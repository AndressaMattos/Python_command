def calculo_agua(astronautas, estoque, dias):
    for argument in (astronautas, estoque, dias):
         
        try:
                # If argument is an int, the following operation will work
                argument / 10
        except TypeError:
                # TypeError will be raised only if it isn't the right type 
                # Raise the same exception but with a better error message
                raise TypeError(f"All arguments must be of type int, but received: '{argument}'")


    total = (astronautas * 11) * dias
    resto = estoque - total

    if resto < 0:
       raise  RuntimeError(f"Não há água suficiente {resto} para {astronautas} astronautas")
    
    return f' {resto}Será usando {total} litros de água em {dias} dias para {astronautas} astronautas'

#print(calculo_agua(5,150,3))

try:
    calculo_agua(5, 100, 2)
except RuntimeError as err:
    print(err)

#water_left("3", "200", None)