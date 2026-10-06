def clasificar_notas(nota):
    if nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"
print(clasificar_notas(4))