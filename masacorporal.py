def clasificar_masa_corporal(peso, altura):
    imc = peso / altura**2
    if imc < 18.5:
        return "bajo peso"
    elif imc < 25:
        return "normal"
    else:
        return "obeso"
        
print(clasificar_masa_corporal(70, 1.75))   