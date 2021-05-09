from datetime import datetime

def encabezado(ciudad, upper = False):
    '''
    Devuelve un encabezado con ciudad y fecha en el formato "Ciudad", "día (número)" de "Mes (palabra)" de "año".

    Args:
        ciudad = Ciudad donde se confecciona el documento, como str.
        upper(default = False) = Devuelve todo el encabezado en mayúsculas.
        '''
    dia = datetime.now().day
    mes = datetime.now().month
    lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviemmbre', 'Diciembre']
    mes = lista_meses[mes-1]
    anio = datetime.now().year
    if upper == True:
        print((f"{ciudad}, {dia} de {mes} de {anio}.").upper())
    else:
        print((f"{ciudad}, {dia} de {mes} de {anio}.").capitalize())