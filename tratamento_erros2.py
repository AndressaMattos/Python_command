loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""


# Enter code below
separacao_arquivo = {}

for line in loaded_config.split('\n'):
    try:
        key, value = line.split("=")
        separacao_arquivo[key] = value
    except ValueError:
        print(f"Impossívrl dividir {line}")

print(separacao_arquivo)