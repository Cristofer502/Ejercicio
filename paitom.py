def case_one():
    return "Opción 1 seleccionada"

def case_two():
    return "Opción 2 seleccionada"

def case_three():
    return "Opción 3 seleccionada"

def default_case():
    return "Opción por defecto"

switch = {
    1: case_one,
    2: case_two,
    3: case_three
}

# Variable para la opción seleccionada
option = 2

# Ejecutar la función correspondiente o la opción por defecto
result = switch.get(option, default_case)()
print(result)
