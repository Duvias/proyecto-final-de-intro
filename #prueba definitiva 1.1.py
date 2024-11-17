alimentos_precio= {"Empanada":1200,"Papa":1600,"Papa rellena":3500,"Salchichón":600,"Ala de pollo":4000,"Pescado":7000,"Aborrajado":2000}
bebidas_precio = {"Coca-Cola 500ml":3000,"Coca-Cola 250ml":1600,"Jugo hit 1.2L":3500,"Jugo hit 400ml":2200,"Jugo hit 250ml":1500,"Jugo hit 250ml":1500,"Postobon Acqua":1500,"Speedmax": 1500,"Natumalta 200ml":1300,"Natumalta 400ml":2000,"Agua cristal": 1500,"Agua con gas cristal": 1500,"Postobon personal vidrio":1200,"Postobon litro vidrio":4000,"Postobon litro plastico":4500,"Pepsi grande":3500,"Natumalta grande":3650,"Tropikola":1500,"Squash personal":2500,"Mr tea personal":2000,"Tutti Frutti":1200,"H20h":1800}
alimentos_cantidad= {"Empanada":21,"Papa":18,"Papa rellena":9,"Salchichón":9,"Ala de pollo":4,"Pescado":5,"Aborrajado":10}
bebidas_cantidad = {"Coca-Cola 500ml":13,"Coca-Cola 250ml":20,"Jugo hit 1.2L":18,"Jugo hit 400ml":12,"Jugo hit 250ml":13,"Jugo hit 250ml":15,"Postobon Acqua":16,"Speedmax": 18,"Natumalta 200ml":8,"Natumalta 400ml":27,"Agua cristal": 40,"Agua con gas cristal": 20,"Postobon personal vidrio":32,"Postobon litro vidrio":20,"Postobon litro plastico":23,"Pepsi grande":15,"Natumalta grande":14,"Tropikola":13,"Squash personal":10,"Mr tea personal":7,"Tutti Frutti":9,"H20h": 16}

def gestion_inv():
    print ("\nLista Actualizada:")
    print ("Alimentos:")
    # Se recorren las posiciones de las dos listas mostrando la posición, la cantidad y su precio
    for posicion,producto in enumerate(alimentos_precio):
        cantidad = alimentos_cantidad[producto]
        precio = alimentos_precio[producto]
        print (f"Posición[{posicion}]: {producto} - Valor: ${precio} - Cantidad: {cantidad}")
    print ("\nBebidas:")
    for posicion,producto in enumerate(bebidas_precio):
        cantidad = bebidas_cantidad[producto]
        precio = bebidas_precio[producto]
        print (f"Posición [{posicion}]: {producto} - Valor: ${precio} - Cantidad: {cantidad}")
    

gestion_inv()   

def atencion():
    # Inicializamos los totales para bebidas y alimentos solo con las compras del usuario
    total_bebidas_usuario = 0
    total_alimentos_usuario = 0

    while True:
        try:
            accion = int(input("(1) Atención en Mesa\n(2) Comprar para llevar\nEscoge la acción a realizar escribiendo 1 o 2: "))
            if accion == 1 or accion == 2:
                break
        except ValueError:
            print("\nPor favor digita numeros unicamente")

    if accion == 1:
        print("------------Menú--------------\nBebidas-----------------------")
        bebidas_disponibles = [(bebida, precio) for bebida, precio in bebidas_precio.items() if bebidas_cantidad.get(bebida, 0) > 0]
        print(f"-{"\n-".join([f"{i+1}. {bebida} - ${precio}" for i, (bebida, precio) in enumerate(bebidas_disponibles)])}")
        
        while True:
            indice_bebida = int(input("Qué bebida deseas?(Utiliza los números para elegir): "))
            bebida, precio = bebidas_disponibles[indice_bebida - 1]
            cantidad_bebida_usuario = int(input(f"Cuántas {bebida} deseas?: "))
            total_bebidas_usuario += cantidad_bebida_usuario * precio  # Acumulamos el total de las bebidas
            mas_bebida = input("¿Deseas otra bebida?(SI/NO): ")
            while mas_bebida.upper() not in ["SI", "NO"]:
                print("Por favor responde SI o NO")
                mas_bebida = input("¿Deseas otra bebida?(SI/NO): ")
            if mas_bebida.upper() == "NO":
                break

        print(f"Alimentos-----------------------\n-{"\n-".join([f"({i+1}) {alimento}: ${precio}" for i, (alimento, precio) in enumerate(alimentos_precio.items()) if alimentos_cantidad.get(alimento, 0) > 0])}")
        alimentos_disponibles = [(alimento, precio) for alimento, precio in alimentos_precio.items() if alimentos_cantidad.get(alimento, 0) > 0]
        while True:
            indice_alimento = int(input("Qué alimento deseas?(Utiliza los números para elegir): "))
            alimento, precio = alimentos_disponibles[indice_alimento - 1]
            cantidad_alimento_usuario = int(input(f"Cuántas {alimento} deseas?: "))
            total_alimentos_usuario += cantidad_alimento_usuario * precio  # Acumulamos el total de los alimentos
            mas_alimento = input("¿Deseas otro alimento?(SI/NO): ")
            while mas_alimento.upper() not in ["SI", "NO"]:
                print("Por favor responde SI o NO")
                mas_alimento = input("¿Deseas otro alimento?(SI/NO): ")
            if mas_alimento.upper() == "NO":
                break

    print("\n------------ Cierre de Caja ------------")
    total = total_bebidas_usuario + total_alimentos_usuario  
    print(f"Total ventas realizadas: ${total}")
    print("Gracias, hasta pronto :)")

atencion()
