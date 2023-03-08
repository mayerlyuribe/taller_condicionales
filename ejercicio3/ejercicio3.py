#input

p_art = int(input("Ingrese el  valor del artículo: "))

if p_art<3000:
    ganancia= p_art*0.15
    p_venta= p_art+ ganancia
else:
    if p_art<6000:
        ganancia=500
        p_venta=p_art+ganancia
    else:
        ganancia= p_art*0.25
        p_venta=p_art+ganancia

print("El precio de vcenta es: " + str(p_venta))