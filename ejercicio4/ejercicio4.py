# input

peso = int(input("digite el valor de peso: "))
altura = float(input("digite la altura: "))

# processing
imc = peso/altura**2

if imc<16:
    msj= "criterio de ingreso al hospital"
else:
    if imc<17:
        msj = "infrapeso"
    else:
        if imc<18:
            msj="bajo peso"
        else:
            if imc<25:
                msj= "peso saludable"
            else:
                if imc<30:
                    msj= "sobrepeso (obesidad grado 1)"
                else:
                    if imc<35:
                        msj= "sobrepeso (grado 2)"
                    else:
                        if imc<40:
                            msj="obesidad premórbida (obecidad de grado 3)"
                        else:
                            if imc>40:
                                msj="obesidad mórbida (obecidad grado 4)"
                            else:
                                msj="obesidad mórbida(obesidad de grado 5)"

# output
print("su indice de peso es: "+str(imc))
print(msj)