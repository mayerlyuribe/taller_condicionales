#input

ing = int(input ("¿Cuánto gana mensualmente?: "))
#processing

if ing>945200:
    deudas = int(input ("¿Tiene alguna deuda actualmente?: "))
    if deudas == 0:
        rta = "préstamo aprobado"
    else:
        rta = "préstamo no aprobado"
else:
    rta = "préstamo no aprobado"

#output
print(rta) 