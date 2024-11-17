alimentos_precio= {"Empanada":1200,"Papa":1600,"Papa rellena":3500,"Salchichón":600,"Ala de pollo":4000,"Pescado":7000,"Aborrajado":2000}
bebidas_precio = {"Coca-Cola 500ml":3000,"Coca-Cola 250ml":1600,"Jugo hit 1.2L":3500,"Jugo hit 400ml":2200,"Jugo hit 250ml":1500,"Jugo hit 250ml":1500,"Postobon Acqua":1500,"Speedmax": 1500,"Natumalta 200ml":1300,"Natumalta 400ml":2000,"Agua cristal": 1500,"Agua con gas cristal": 1500,"Postobon personal vidrio":1200,"Postobon litro vidrio":4000,"Postobon litro plastico":4500,"Pepsi grande":3500,"Natumalta grande":3650,"Tropikola":1500,"Squash personal":2500,"Mr tea personal":2000,"Tutti Frutti":1200,"H20h":1800}
alimentos_cantidad= {"Empanada":21,"Papa":18,"Papa rellena":9,"Salchichón":9,"Ala de pollo":4,"Pescado":5,"Aborrajado":10}
bebidas_cantidad = {"Coca-Cola 500ml":13,"Coca-Cola 250ml":20,"Jugo hit 1.2L":18,"Jugo hit 400ml":12,"Jugo hit 250ml":13,"Jugo hit 250ml":15,"Postobon Acqua":16,"Speedmax": 18,"Natumalta 200ml":8,"Natumalta 400ml":27,"Agua cristal": 40,"Agua con gas cristal": 20,"Postobon personal vidrio":32,"Postobon litro vidrio":20,"Postobon litro plastico":23,"Pepsi grande":15,"Natumalta grande":14,"Tropikola":13,"Squash personal":10,"Mr tea personal":7,"Tutti Frutti":9,"H20h": 16}

def atencion():
    while True:
        try:
            accion=int(input("(1) Atención en Mesa\n(2) Comprar para llevar\nEscoge la acción a realizar escribiendo 1 o 2: "))
            if accion == 1 or accion == 2:
                break
        except(ValueError):
            print("\nPor favor digita numeros unicamente")

    if accion == 1:
        print("------------Menú--------------\nBebidas-----------------------")
        bebidas_disponibles = [(bebida, precio) for bebida, precio in bebidas_precio.items() if bebidas_cantidad.get(bebida, 0) > 0]
        print(f"-{"\n-".join([f"{i+1}. {bebida} - ${precio}" for i, (bebida, precio) in enumerate(bebidas_disponibles)])}")
        while True:
            #
            indice_bebida=int(input("Que bebida deseas?(Utiliza los números para elegir): "))
            
            
            bebida, precio= bebidas_disponibles[indice_bebida-1]
            
            #
            bebida_cantidad=int(input(f"Cuantas {bebida} desea?: "))
            
            #
            mas_bebida = input("Desea otra bebida?(SI/NO): ")
            while (mas_bebida.upper() == "SI" or mas_bebida.upper() == "NO") == False:
                    print("Por favor responde SI o NO")
                    mas_bebida = input("Desea otro alimento?(SI/NO): ")
            if mas_bebida.upper() == "NO":
                break
        
        print(f"Alimentos-----------------------\n-{"\n-".join([f"({i+1}) {alimento}: ${precio}" for i, (alimento, precio) in enumerate(alimentos_precio.items()) if alimentos_cantidad.get(alimento, 0) > 0])}")
        alimentos_disponibles = [(alimento, precio) for alimento, precio in alimentos_precio.items() if alimentos_cantidad.get(alimento, 0) > 0]
        while True:
            # Validacion de que la respuesta del indice es correcta
            while True:
                try:
                    indice_alimento=int(input("Que alimento deseas?(Utiliza los números para elegir): "))
                    if len(alimentos_cantidad) >= indice_alimento > 0:    
                        break
                    else:
                        print(f"Por favor, solo digite el numero de alimentos disponibles, intente de nuevo")
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
            
            # Pedir comprobar si desea mas alimento y asegurarse que la respuesta sea SI o NO
            mas_alimento = input("Desea otro alimento?(SI/NO): ")
            while (mas_alimento.upper() == "SI" or mas_alimento.upper() == "NO") == False:
                print("Por favor responde SI o NO")
                mas_alimento = input("Desea otro alimento?(SI/NO): ")
            if mas_alimento.upper() == "NO":
                break

atencion()
