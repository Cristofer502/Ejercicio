def case_1():
    return "Ejecutando caso 1"
 
def case_2():
    return "Ejecutando caso 2"
 
def case_3():
    return "Ejecutando caso 3"
 
def default_case():
    return "Caso no encontrado"
 
def switch_case(case):
    switcher = {
        1: case_1,
        2: case_2,
        3: case_3,
    }
    return switcher.get(case, default_case)()
 
# Ejemplo de uso
case_number = 2
print(switch_case(case_number))                     