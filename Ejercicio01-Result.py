listaRegistro = []
clientes = 0
conta1 = 1
 
 
while clientes < conta1:
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    mensaje = "¿Deseas agregar otro cliente?"

    print(mensaje)
    respuesta = input("Respuesta:  ")
    if respuesta == "si":
         clientes += 1
         conta1 += 1
          
   
    else:
     clientes += 2
       
      
     for registro in listaRegistro:
      print(registro)

     mensaje2 = "Los costos obtenidos durante la jordanada son "
     for registro in listaRegistro:
       costosTotal = sum(int(costo)) 
       print(mensaje2 + str(costosTotal))