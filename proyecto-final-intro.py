def atencion():
    while True:
        try:
            accion=int(input("(1) Atención en Mesa\n(2) Comprar para llevar\nEscoge la acción a realizar escribiendo 1 o 2: "))
            if accion == 1 or accion == 2:
                break
        except(ValueError):
            print("\nPor favor digita numeros unicamente")
    
    if accion == 1:
        print("Menú--------------------------\n")


atencion()
