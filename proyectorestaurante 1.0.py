import os
"""  
       -> Restaurante SESHAT<-
  @Duvan Pacheco

"""
"""
---------------------------------------------------
                  Menu principal
---------------------------------------------------
"""



def tipoDeUsuarios():
  """
  Funcion para mostrar el menu principlal
  """
  os.system("cls")  
  print("           BIENVENIDO A SESHAT")
  print()
  print("Selecciona una opcion (1 - 3):")
  print("1. Cajero")
  print("2. Administrador")
  print("3. Salir")
  usuario=input()
  if usuario== "1":
    print()
    os.system("cls")
    menuCliente()
  elif usuario=="2":
    print()
    contrasenaAdmi()
  elif usuario=="3":
    salir()
  else:
    print()
    print ("Entrada incorrecta")
    d=input("¿Deseás intentar de nuevo? (s/n):    ")
    if d== "s":
      tipoDeUsuarios()
    elif d != "s":
      os.system("cls")
      salir()



def menuCliente():
      """
      Funcion para el menu del cliente
      """
      os.system("cls")
      print ("       MENÚ DE CLIENTE")
      print()
      print ("    Selecciona una opcion (1 - 4):")
      print ("1. Comprar como cliente no asociado")
      print ("2. Comprar como cliente asociado")
      print ("3. Registrar nuevo cliente")
      print ("4. Salir")
      print()
      entradaCliente()



def entradaCliente():
      """
      Funcion para redirecionar las entradas del cliente
      """
      x= input()
      if x == "1":
            os.system("cls")
            compra()
      elif x =="2":
            y=BuscarCliente()
            compra2(y) 
      elif x =="3":
            nuevocliente()

      elif x=="4":
            tipoDeUsuarios()

      else:
        print()
        print ("Entrada incorrecta")
        d=input("Deseas salir (s/n):    ")
        if d== "s":
              entradaCliente()
        elif d != "s":
              os.system("cls")
              menuAdministrador()
"""
--------------------------------------------------------------
                   BUSCAR CLIENTE Y AGREGAR CLIENTE
--------------------------------------------------------------                     
"""


def BuscarCliente():
      
    """
    Funcion para buscar cliente en la lista
    """
    os.system("cls")
    x=0
    numeroID = int (input("INGRESA EL NUMERO DE IDENTIFICACIÓN:    "))
    for i in Listacliente:
        if numeroID == Listacliente[x][1]:                  
              NOMBRE= Listacliente[x][0]
              PUNTOS= Listacliente[x][2]+1
              return PUNTOS, NOMBRE
              
        x+=1
    print ("          Este usuario no existe")

    d=input("ingresa 's' para voler a intentar, 'n' para salir     ")
    if d== "s":
      menuCliente()
    elif d != "s":
      os.system("cls")
      menuCliente()
    print()



def nuevocliente():
  """
  Funcion para agregar nuevo CLIENTE
  """
  os.system("cls")
  print("     AGREGA NUEVO CLIENTE")
 
  
  print("Ingreso el nombre del cliente")
  nombre = input()
  print()
  print("Ingrese el numero de identificación")
  numero = int(input())
  print()
  Puntos = 0
  print()
  Listacliente.append([nombre, numero, Puntos])
  
  menuCliente()

"""
---------------------------------------------------------------------
                      CONTRASEÑA DE ADMINISTRADOR
---------------------------------------------------------------------
                
"""
    

def contrasenaAdmi():
  """
  Funcion para comprobar contraseña
  """
  comprobarcontraseña=input("Escribe la contraseña de administracion, o (s) para salir:  ")
  if comprobarcontraseña == "s":
    tipoDeUsuarios()

  elif comprobarcontraseña == contraseña:
    menuAdministrador()
  
  else:
    print("Contraseña incorrecta")
    contrasenaAdmi()



def cambiocontrasena():
  """
  Funcion para cambiar la contraseña
  """
  os.system("cls") 
  print("CAMBIO DE CONTRASEÑA")
  print()
  global contraseña
  comprobar2=input("Escribe tu contraseña actual, o (s) para salir:    ")

  if comprobar2 == contraseña:
    c1=input("Escribe la nueva contraseña:   ")
    c2=input("Vuelve a escribir la nueva contraseña:   ")
    if c1==c2:
      contraseña= c1
      d=input("Deseas salir (s/n):    ")
      if d== "s":
        os.system("cls")
        menuAdministrador()
      elif d != "s":
        os.system("cls")
        cambiocontrasena()

  elif comprobar2== "s":
    tipoDeUsuarios()
  else:
    print("Contraseña incorrecta")
    cambiocontrasena()
    

def menuAdministrador():
  """
  Funcion para mostrar el menu del administrador
  """
  os.system("cls")
  print("       Bienbenido a Seshat, ¿que deseas hacer?")
  print()
  print("      Escoje una opción del 1-6")
  print("1. Agregar un nuevo producto")
  print("2. Ver inventario")
  print("3. Agregar al inventario")
  print("4. Total de ventas del dia")
  print("5. Cambio de contraseña")
  print("6. Salir")
  print()
  entradaAdministrador()  

 
def entradaAdministrador():
  """
  Funcion para controlar la entrada del menu del administrador
  """
  entrada=input()
  if entrada == "1":
    nuevoproducto()
  elif entrada == "2":
    inventario()
  elif entrada == "3":    
    AgregarInventario()
  elif entrada == "4":
    ventasDiarias()
  elif entrada == "5":
    cambiocontrasena()
  elif entrada == "6":
    tipoDeUsuarios()
  else:
    print()
    print ("Entrada incorrecta")
    d=input("¿Deseas salir? (s/n):    ")
    if d== "s":
      menuAdministrador()
    elif d != "s":
      os.system("cls")
      tipoDeUsuarios()
    print()



def salir():
  """
  Funcion para salir del programa
  """
  return exit()        

""" 
--------------------------------------------------------
                      Comprar
--------------------------------------------------------
"""


def compra():
  """
  Funcion para que los usuarios compren Platos y Bebidas no asociados
  """
  print("    Bienvenido a Seshat, ¿que deseas Comprar?")
  print()
  precioTotal = 0
  print("Escoge un Plato:")
  impplatos()
  print()
  num = int(input()) - 1
  print("has seleccionado:")
  print(str(num+1) + ")", Platos[num][0], " "*(20-len(Platos[num][0])), Platos[num][1]," ", Platos[num][2] )
  print()
  print("¿Cuantas porciones?")
  porcion_1 = int(input())
  if porcion_1 > Platos[num][2] or porcion_1<0:
    os.system("cls")
    print("     Lo sentimos, no hay suficientes porciones")
    print()
    compra()
  precioTotal += (Platos[num][1]*porcion_1)
  print()
  print("¿Desea algo de beber?  (s/n)")    
  x = input()
  print()  
  if x == "s":
    print("Escoje la bebida:")
    impbebidas()
    print()
    num = int(input()) - 1
    print("has seleccionado:")
    print(str(num+1) + ")", Bebidas[num][0], " "*(20-len(Bebidas[num][0])), Bebidas[num][1]," ", Bebidas[num][2] )
    print()
    print("¿Cuantas porciones?")
    porcion_2 = int(input())
    if porcion_2 > Bebidas[num][2] or porcion_2 <0:
      os.system("cls")
      print("Lo sentimos, no hay suficientes porciones")
      print()
      compra()      
    precioTotal += (Bebidas[num][1]*porcion_2)
    Bebidas[num][2] -= porcion_2
    print()
    print("      TOTAL A PAGAR: ", precioTotal)
    Platos[num][2] -= porcion_1
  elif x == "n":
    print("      TOTAL A PAGAR: ", precioTotal)
    Platos[num][2] -= porcion_1
  ventas.append(precioTotal)
  print()
  d=input("Deseas salir (s/n):    ")
  if d== "s":
    os.system("cls")
    tipoDeUsuarios()
  elif d != "s":
    os.system("cls")
    compra() 



def compra2(y):
  """
  Funcion para que los usuarios compren Platos y Bebidas asociados
  :param tupla y: y[0]= Nombre, y[1]=Puntos
  """
  print("    Bienbenido a Seshat, ¿que deseas Comprar?")
  print ("Nombre: ", y[1])
  print("Puntos: " , y[0])
  
  precioTotal = 0
  print("Escoge un Plato:")
  impplatos()
  print()
  num = int(input()) - 1
  print("has seleccionado:")
  print(str(num+1) + ")", Platos[num][0], " "*(20-len(Platos[num][0])), Platos[num][1]," ", Platos[num][2] )
  print()
  print("¿Cuantas porciones?")
  porcion_1 = int(input())
  if porcion_1 > Platos[num][2] or porcion_1<0:
    os.system("cls")
    print("     Lo sentimos, no hay suficientes porciones")
    print()
    compra()
  precioTotal += (Platos[num][1]*porcion_1)
  print()
  print("¿Desea algo de beber?  (s/n)")    
  x = input()
  print()  
  if x == "s":
    print("Escoje la bebida:")
    impbebidas()
    print()
    num = int(input()) - 1
    print("has seleccionado:")
    print(str(num+1) + ")", Bebidas[num][0], " "*(20-len(Bebidas[num][0])), Bebidas[num][1]," ", Bebidas[num][2] )
    print()
    print("¿Cuantas porciones?")
    porcion_2 = int(input())
    if porcion_2 > Bebidas[num][2] or porcion_2 <0:
      os.system("cls")
      print("Lo sentimos, no hay suficientes porciones")
      print()
      compra()      
    precioTotal += (Bebidas[num][1]*porcion_2)
    Bebidas[num][2] -= porcion_2
    print()
    if y[0]==5:
          precioTotal= precioTotal//2
    print("      TOTAL A PAGAR: ", precioTotal)
    Platos[num][2] -= porcion_1
  elif x == "n":
    if y[0]==5:
          precioTotal= precioTotal//2
    print("      TOTAL A PAGAR: ", precioTotal)
    Platos[num][2] -= porcion_1
  ventas.append(precioTotal)
  print()
  d=input("Deseas salir (s/n):    ")
  if d== "s":
    os.system("cls")
    tipoDeUsuarios()
  elif d != "s":
    os.system("cls")
    tipoDeUsuarios()
"""
---------------------------------------------------------
              Agregar un nuevo producto
---------------------------------------------------------
"""   


def nuevoproducto():
  """
  Funcion para agregar un nuevo producto (Plato o bebida) al inventario
  """
  os.system("cls")
  print("     AGREGA NUEVO PRODUCTO")
  print("1. Plato")
  print("2. Bebida")
  print("q. Salir")
  print()
  
  entrada = input()
  if entrada == "1":
    print("Ingrese el nombre del producto")
    producto = input()
    print()
    print("Ingrese el valor de la porcion")
    valor = int(input())
    print()
    print("Ingrese el numero de porciones disponibles")
    porciones = int(input())
    print()
    Platos.append([producto, valor, porciones])
  elif entrada == "2":
    print("Ingrese el nombre del producto")
    producto = input()
    print()
    print("Ingrese el valor de la porcion")
    valor = int(input())
    print()
    print("Ingrese el numero de porciones disponibles")
    porciones = int(input())
    print()
    Bebidas.append([producto, valor, porciones])
  menuAdministrador()


""" 
-------------------------------------------------------
                 Ver inventario
-------------------------------------------------------
"""  


def borrar():
  """
  Funcion para borrar los Platos y Bebidas con 0 porciones
  """
  indicesPlatos = []
  indicesBebidas = []
  for a in range(len(Platos)):
    if Platos[a][2] == 0:
      indicesPlatos.append(a)
  for b in range(len(Bebidas)):
    if Bebidas[b][2] == 0:
      indicesBebidas.append(a)
  for c in indicesPlatos:
    del(Platos[c])           
  for d in indicesBebidas:
    del(Bebidas[d])



def impplatos():
  """
  Funcion para imprimir los Platos con 1 o más porciones
  """
  borrar()
  for a in range(len(Platos)):
    print(str(a+1) + ")", Platos[a][0], " "*(20-len(Platos[a][0])), Platos[a][1]," ", Platos[a][2] )



def impbebidas():
  """
  Funcion para imprimir las Bebidas con 1 o más porciones
  """
  borrar()
  for b in range(len(Bebidas)):
    print(str(b+1) + ")", Bebidas[b][0], " "*(20-len(Bebidas[b][0])), Bebidas[b][1]," ", Bebidas[b][2] )


      
def inventario():
  """
  Funcion para imprimir el inventario
  """
  print("INVENTARIO")
  borrar()
  print("  Platos")
  impplatos()
  print()
  print("  Bebidas")
  impbebidas()
  print()
  d=input("Deseas salir (s/n):   ")
  if d== "s":
    os.system("cls")
    menuAdministrador()
  elif d != "s":
    menuAdministrador()
    

"""
-------------------------------------------------------
                Agregar al inventario
-------------------------------------------------------
"""  

def AgregarInventario():
  """
  Funcion para agregar el total de porciones de Platos o Bebidas
  """
  os.system("cls")
  print ("     AGREGAR AL INVENTARIO")
  print("Tipo de producto (1 o 2)")
  print("1. Plato")
  print("2. Bebida")
  print("q. Salir")
  
  entrada = input()
  print()
  if entrada == "1":
    print("Seleccione un producto")  
    impplatos()
    num = (int(input())) -1
    print()
    print("Has selecciono:")
    print(str(num+1) + ")", Platos[num][0], " "*(20-len(Platos[num][0])), Platos[num][1]," ", Platos[num][2] )
    print()
    print("Ingrese la cantidad de porciones a registrar:")
    Platos[num][2] = int(input()) + Platos[num][2] 
    print()
  elif entrada == "2":
    print("Seleccione un producto")  
    impbebidas()
    num = (int(input())) -1
    print()
    print("Usted selecciono:")
    print(str(num+1) + ")", Bebidas[num][0], " "*(20-len(Bebidas[num][0])), Bebidas[num][1]," ", Bebidas[num][2] )
    print()
    print("Ingrese la cantidad de porciones a registrar:")
    Bebidas[num][2] = int(input()) + Bebidas[num][2]
    print()
  inventario()

""" 
--------------------------------------------------------
               Total de ventas del dia
--------------------------------------------------------
""" 


def ventasDiarias():
  """
  Funcion para ver o reiniciar el total de ventas diarias
  """
  os.system("cls")
  total = 0
  global ventas
  for e in ventas:
    total += e 
  print("Total ventas del día:", total)
  print() 
  print("Oprima r para reiniciar el total de ventas diarias o s para salir")
  if input() == "r":
    ventas = []
  print()
  menuAdministrador()


# Funcion principal que ejecuta todo el programa
def main():

  #Declarar las variables globales del programa
  """ Listas globales
  Listas de productos como variables globales, organizados de la siguiente manera:
  Platos = [ [producto, valor, porciones], [producto, valor, porciones]
  Bebidas = [ [producto, valor, porciones], [producto, valor, porciones] 
  ventas = [] # Va guardando el valor de cada venta realizada
  Lista de clientes como variables globales, organizados de la siguente manera:
  Listacliente= [[Nombre, Documento, Puntos],[Nombre, Documento, Puntos]]
  """
  global Platos, Bebidas, ventas, Listacliente 
  Platos = [ ["Arroz con pollo", 8000, 12], ["hamburguesa", 7000, 50], ["Arroz con Mariscos", 4000, 20] ]
  Bebidas =[ ["Gaseosa",2500, 30], ["Jugo Natural",2000, 40], ["Cafe", 1500, 20] ]
  ventas = [0]

  #Lista gllobal de clientes
  Listacliente = [ ["Duvan Pacheco",1003828944,4],["pablo pachon", 1000, 3] , ["brayan angarita",1212,0]]

  #Contraseña por defecto
  global contraseña
  contraseña= "12345678"
  tipoDeUsuarios()

main()
