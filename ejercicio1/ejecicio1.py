#input 
print("----------------------------------------------")
print("----------- ejercicio 1 ----------------------")
print("----------------------------------------------")



print("----------------------------------------------")
print("---------- Digite el valor de x, y -----------")
print("----------------------------------------------")

#input

x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

#processing

if x==0:
    if y==0:
        msj= "las coordenadas están en el origen"
    else:
        msj = "La coordenada está en el eje y"
else:
    if y==0:
        msj = "La coordenada está en el eje x"
    else:
        if x>0:
            if y>0:
                msj = "Las coordenadas están en el cuadrante 1"
            else:
                msj = "Las coordenadas están en el cuadrante 4"
        else:
            if y<0:
                msj = "Las coordenadas están en el cuadrante 3"
            else:
                msj = "Las coordenadas están en el cuadrante 2"

#output

print(msj)
Footer
