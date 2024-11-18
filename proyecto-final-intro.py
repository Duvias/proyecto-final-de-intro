import sqlite3
alimentos_precio= {"Empanada":1200,"Papa":1600,"Papa rellena":3500,"Salchichón":600,"Ala de pollo":4000,"Pescado":7000,"Aborrajado":2000}

bebidas_precio = {"Coca-Cola 500ml":3000,"Coca-Cola 250ml":1600,"Jugo hit 1.2L":3500,"Jugo hit 400ml":2200,"Jugo hit 250ml":1500,"Jugo hit 250ml":1500,"Postobon Acqua":1500,"Speedmax": 1500,"Natumalta 200ml":1300,"Natumalta 400ml":2000,"Agua cristal": 1500,"Agua con gas cristal": 1500,"Postobon personal vidrio":1200,"Postobon litro vidrio":4000,"Postobon litro plastico":4500,"Pepsi grande":3500,"Natumalta grande":3650,"Tropikola":1500,"Squash personal":2500,"Mr tea personal":2000,"Tutti Frutti":1200,"H20h":1800}

alimentos_cantidad= {"Empanada":21,"Papa":18,"Papa rellena":9,"Salchichón":9,"Ala de pollo":4,"Pescado":5,"Aborrajado":10}

bebidas_cantidad = {"Coca-Cola 500ml":13,"Coca-Cola 250ml":20,"Jugo hit 1.2L":18,"Jugo hit 400ml":12,"Jugo hit 250ml":13,"Jugo hit 250ml":15,"Postobon Acqua":16,"Speedmax": 18,"Natumalta 200ml":8,"Natumalta 400ml":27,"Agua cristal": 40,"Agua con gas cristal": 20,"Postobon personal vidrio":32,"Postobon litro vidrio":20,"Postobon litro plastico":23,"Pepsi grande":15,"Natumalta grande":14,"Tropikola":13,"Squash personal":10,"Mr tea personal":7,"Tutti Frutti":9,"H20h": 16}

mesas = {"Mesa 1": False, "Mesa 2": True, "Mesa 3": True, "Mesa 4": True, "Mesa 5": True, "Mesa 6": True, "Mesa 7": True, "Mesa 8": True, "Mesa 9": True, "Mesa 10": True}

separador="\n-"
# def registro_ventas():
conexion = sqlite3.connect("registro_ventas.db")    
cursor = conexion.cursor()

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

def atencion():
    # Inicializamos los totales para bebidas y alimentos solo con las compras del usuario
    total_bebidas_usuario = 0
    total_alimentos_usuario = 0
    
    cursor.execute("SELECT producto FROM ventas")
    resultado=cursor.fetchall()
    print(f"el producto es {''.join(resultado[0])}")
    while True:
        try:
            accion=int(input("(1) Atención en Mesa\n(2) Comprar para llevar\nEscoge la acción a realizar escribiendo 1 o 2: "))
            if accion == 1 or accion == 2:
                break
        except(ValueError):
            print("\nPor favor digita numeros unicamente")

    # Codigo del menu
    mesas_disponibles = [(mesa) for mesa, disponibilidad in mesas.items() if mesas.get(mesa, 0) == False]
    if not mesas_disponibles:
        print("En el momento no hay ninguna mesa disponible, realiza el cobro de la cuenta de una mesa para desocuparla.")
    else:
        print("------------Menú--------------\nBebidas-----------------------")
        bebidas_disponibles = [(bebida, precio) for bebida, precio in bebidas_precio.items() if bebidas_cantidad.get(bebida, 0) > 0]
        print(f"-{separador.join([f'({i+1}) {bebida} - ${precio}' for i, (bebida, precio) in enumerate(bebidas_disponibles)])}")
        while True:
            # Validacion de que la respuesta del indice de bebidas es correcto
            while True:
                try:
                    indice_bebida=int(input("Que bebida deseas?(Utiliza los números para elegir): "))
                    if len(bebidas_cantidad) >= indice_bebida > 0:    
                        break
                    else:
                        print(f"Por favor, solo digite el numero de las bebidas disponibles, intente de nuevo")
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero")
            bebida, precio= bebidas_disponibles[indice_bebida-1]
            query="INSERT INTO ventas (producto) VALUES (?)"
            cursor.execute(query, (bebida,))
            
            
            cursor.execute("SELECT producto FROM ventas")
            resultado=cursor.fetchall()
            # Comprobacion de que entrada de la cantidad sea valida(Falta restar la cantidad de lo que se pide al inventario)
            while True:
                try:
                    bebida_cantidad=int(input(f"Cuantas {bebida} desea?: "))
                    if bebidas_cantidad[bebida] >= bebida_cantidad > 0:    
                        break
                    else:
                        print(f"Esa cantidad de {bebida} no esta disponible, tenemos {bebidas_cantidad[bebida]} {bebida}, intente de nuevo")
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero")
            total_bebidas_usuario += bebida_cantidad * precio  # Acumulamos el total de las bebidas
            bebidas_cantidad[bebida]-=bebida_cantidad
            
            # Pedir comprobar si desea mas alimento y asegurarse que la respuesta sea SI o NO
            mas_bebida = input("Desea otra bebida?(SI/NO): ")
            while mas_bebida.upper() not in ["SI", "NO"]:
                    print("Por favor responde SI o NO")
                    mas_bebida = input("Desea otro alimento?(SI/NO): ")
            if mas_bebida.upper() == "NO":
                break
            
            
        print(f"Alimentos-----------------------")
        print(f'-{separador.join([f"({i+1}) {alimento}: ${precio}" for i, (alimento, precio) in enumerate(alimentos_precio.items()) if alimentos_cantidad.get(alimento, 0) > 0])}')
        alimentos_disponibles = [(alimento, precio) for alimento, precio in alimentos_precio.items() if alimentos_cantidad.get(alimento, 0) > 0]
       
        while True:
            # Validacion de que la respuesta del indice de alimentos es correcto
            while True:
                try:
                    indice_alimento=int(input("Que alimento deseas?(Utiliza los números para elegir): "))
                    if len(alimentos_cantidad) >= indice_alimento > 0:    
                        break
                    else:
                        print(f"Por favor, solo digite el numero de los alimentos disponibles, intente de nuevo")
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero")
            alimento, precio= alimentos_disponibles[indice_alimento-1]
            
            # Comprobacion de que entrada de la cantidad sea valida(Falta restar la cantidad de lo que se pide al inventario)
            while True:
                try:
                    alimento_cantidad=int(input(f"Cuantas {alimento} desea?: "))
                    if alimentos_cantidad[alimento] >= alimento_cantidad > 0:    
                        break
                    else:
                        print(f"Esa cantidad de {alimento} no esta disponible, tenemos {alimentos_cantidad[alimento]} {alimento}, intente de nuevo")
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero")
            total_alimentos_usuario += alimento_cantidad * precio  # Acumulamos el total de los alimentos
            alimentos_cantidad[alimento]-=alimento_cantidad
            
            # Pedir comprobar si desea mas alimento y asegurarse que la respuesta sea SI o NO
            mas_alimento = input("Desea otro alimento?(SI/NO): ")
            while mas_alimento.upper() not in ["SI", "NO"]:
                print("Por favor responde SI o NO")
                mas_alimento = input("Desea otro alimento?(SI/NO): ")
            if mas_alimento.upper() == "NO":
                break
        
        total = total_bebidas_usuario + total_alimentos_usuario 
        
        # Asignar mesas a los pedidos
        if accion == 1:
            print(f"Su orden estara lista pronto, por favor espere en la mesa {mesas_disponibles[0]}.")
            mesas[mesas_disponibles[0]] = True
        elif accion == 2:
            # Se registra la venta
            i=1
        # for i in range(3):
        #     print(f"el producto es {''.join(resultado[i])}")
        print(f"el producto es {''.join(resultado[1])}")

# Codigo Principal 
atencion()
# gestion_inv()
