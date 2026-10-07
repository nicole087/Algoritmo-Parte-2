def clasificar_notas(nota):
    if nota >= 9:
        calificacion = "Sobresaliente"
    elif nota >= 7:
        calificacion = "Notable"
    elif nota >= 5:
        calificacion = "Aprobado"
    else:
        calificacion = "Suspenso"

    return calificacion


print(clasificar_notas(6.5))