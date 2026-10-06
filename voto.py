def verificar_acceso_voto(edad):
    if edad >= 18:
        return True
    else:
        return False
print(verificar_acceso_voto(20))
