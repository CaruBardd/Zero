"""
META GENERAL

AUTOMATIZACIÓN DE PEDIDOS
  ->  Envio una lista completa SIN ASIGNAR MENASJEROS 
  --  ANALIZAR las mejores opciones
  <-  Lista de pedidos ASIGNADOS (↑ Pedidos dinámicos para cada mensajero)

"""
        
# SI NO PUDE ENTREGAR Y TENGO MALETA LLENA (TODO)
#   Entrar en una espera -> Soporte   (Devuelve el pedido / Traelo a Oficina UBICACION FIJA) 
# CASO DE ACCIDENTE O NOVEDAD (TODO)
#   Entrar en una espera -> Soporte   ( MENSAJERO RECOGE EN SU UBICACION (Seguridad del pedido)  / Traelo a Oficina UBICACION FIJA () ) 
# GESTIONAR MENSAJEROS EN MOTO O BICICLETA (TODO)
#   Perfil de mensajero (Vehiculo (Clase), Datos personales, Preferencia distancia (OPX), Tiempo disponible (OPX), (Horario) )


lista = [["A01", 20, False, 35, False], ["A02", 12, False, 38, False], ["A03", 25, False, 40, False], ["B01", 32, False, 12, False], ["B02", 11, False, 9, False]]
maleta_llena = False
omitir = []
ubicacion = 0
tarea = True
while tarea:
    print("ubicacion", ubicacion)
    print("omitir", omitir)
    res = input("Maleta llena  [S/N]: ")
    if res == "Y" or res == "S" or res == "y" or res == "s":
        maleta_llena = True
    else:
        maleta_llena = False
    print(maleta_llena)
    faltante = []

    if maleta_llena:
        for item in lista:
            if not item == omitir:
                if item[2] and not item[4]:
                    faltante.append(item)
                    print(faltante)
    if not maleta_llena:
        for item in lista:
            if not item == omitir:
                if not item[4]:
                    faltante.append(item) 
                    print(faltante)

    menor = 999
    idxd = 0
    print(idxd)
    entregar = []
    for idx in range(len(faltante)):
        if not faltante[idx][2] and not faltante[idx][4]:
            if faltante[idx][1] - ubicacion >= 0:
                if faltante[idx][1] - ubicacion < menor:
                    menor = faltante[idx][1] - ubicacion
                    idxd = idx
            elif (faltante[idx][1] - ubicacion)  * -1 < menor:
                menor = (faltante[idx][1] - ubicacion)  * -1
                idxd = idx
        elif faltante[idx][2] and not faltante[idx][4]:
            if faltante[idx][3] - ubicacion >= 0:
                if faltante[idx][3] - ubicacion < menor:
                    menor = faltante[idx][3] - ubicacion
                    idxd = idx
            elif (faltante[idx][3] - ubicacion)  * -1 < menor:
                menor = (faltante[idx][3] - ubicacion)  * -1
                idxd = idx
    entregar = faltante[idxd]
    print('Debes ir a ')
    if not entregar[2] and not entregar[4]:
        print(entregar[1])
    elif entregar[2] and not entregar[4]:
        print(entregar[3])
    print('')
    print('')
    print('')
    print(faltante)
    res = input('Completado ? [S/N] ')
    omitir = [] 
    for item in lista:
        if item[0] == entregar[0]:
            if not item[2] and not item[4]:
                if res == "Y" or res == "S" or res == "y" or res == "s":
                    item[2] = True
                else:
                    omitir = item
                ubicacion = entregar[1]
            elif item[2] and not item[4]:
                if res == "Y" or res == "S" or res == "y" or res == "s":
                    item[4] = True
                else:
                    omitir = item
                ubicacion = entregar[3]

    # SI COMPLETADO
    
    salir = True
    for item in lista:
        if not item[2] or not item[4]:
            salir = False

    if salir:
        tarea = False
    print(lista)

