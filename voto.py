def verificar_acceso_voto(edad):
    if edad >= 18:
        puede_votar = True
    else:
        puede_votar = False
    return puede_votar 
print(verificar_acceso_voto(20))