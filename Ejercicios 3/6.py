IVA = 21
precio = int(input("Dime el precio de la bicicleta"))
precio_total = (IVA/100)*precio+precio
print("El precio de la bicicleta es", precio, "con el", IVA, "% te sale a", precio_total)