from datetime import datetime

def es_viable(fecha_nacimiento):
    hoy = datetime.now().date()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return "Viable" if 18 <= edad <= 65 else "No viable"
