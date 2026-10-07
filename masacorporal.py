def clasificar_masa_corporal(peso, altura):
    imc = peso / altura**2
    if imc < 18.5:
        categoria = "bajo peso"
    elif imc < 25:
        categoria = "normal"
    else:
        categoria = "obeso"
    return categoria 
print(clasificar_masa_corporal(70, 1.75))