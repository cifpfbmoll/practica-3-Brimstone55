dia = int(input("Dime el día"))
mes = int(input("Dime el mes"))
año = int(input("Dime el año"))
lista31 = [1, 3, 5, 7, 8, 10, 12]

if año % 4 == 0:
    if mes < 12:
        if mes == 2:
            if dia <= 29:
                print("Tu fecha es",dia,"/",mes,"/",año)
            else:
                if dia in lista31:
                    if dia < 31:
                        print("Tu fecha es",dia,"/",mes,"/",año)
                    else:
                        if dia < 30:
                            print("Tu fecha es",dia,"/",mes,"/",año)
                        else:
                            print("Fecha inválida")
    else:
        print("Mes inválido")
else:
    if mes < 12:
        if mes == 2:
            if dia <= 28:
                print("Tu fecha es",dia,"/",mes,"/",año)
            else:
                if dia in lista31:
                    if dia < 31:
                        print("Tu fecha es",dia,"/",mes,"/",año)
                    else:
                        if dia < 30:
                            print("Tu fecha es",dia,"/",mes,"/",año)
                        else:
                            print("Fecha inválida")
    else:
        print("Fecha inválida")