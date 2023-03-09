# Ejercicio 5

CUOTA_FIJA = 10000
gasto = int(input("Digite el gasto de agua en metros cúbicos: "))

if gasto < 50:
    precio = 10000
    msj = ("El precio del agua es: ", (precio))
else:
    if gasto < 200:
         precio = (gasto - 50) *2000 + 10000
         msj = ("El precio del agua es: ", (precio))
    else:
        if gasto >200:
                precio = (gasto - 50) *3000 +10000
                msj = ("El precio del agua es: ", (precio))
        else:
            precio = (gasto - 50) *2000 + 10000
            msj = ("El precio del agua es: ", (precio))
print (msj)
