import os 
import menu
import read
import db
 

#global variables
dataComplete = False


outMenu = False
while outMenu==False:
    os.system('clear')
    menu.menu()

    option =    int(input(">>>> "))
    
    #--------------------------option cargar archivo--------------------------
    if option==1:
        read.read()
        dataComplete = True
    
    #--------------------------option list of sorted--------------------------
    if option==2:
        if dataComplete == False:
            print("Aun no has cargado datos para desplegar las listas\n")
            aaaa = input("Presiona enter para continuar: ")
        elif dataComplete == True:
            os.system('clear')
            print("-------------------------------------Lista de ordenamientos registrados--------------------------------------\n")
            print("Nombre".center(25," "), "Valores".center(25," "),"Valores ordenados".center(25," ") )
            for i in db.arrayRows:
                if i.sort == True:
                    print(i.name.center(25," "),str(i.values).center(25," "),str(i.orderedValues).center(25," "))
            print("\n")
            print("-------------------------------------------Fin de la lista-----------------------------------------------")
            print("\n")
            #print("aqui iran las listar ordenadas")
            aaaa = input("Presiona enter para continuar: ")

    #--------------------------option list of searches--------------------------
    if option==3: 
        
        if dataComplete == False:
            print("Aun no has cargado datos para desplegar las listas\n")
            aaaa = input("Presiona enter para continuar: ")

        elif dataComplete == True:
            os.system('clear')
            print("-------------------------------------lista de busquedas registradas--------------------------------------\n")
            print("nombre".center(25," "), "valores".center(25," "), "valor de busqueda".center(25," ") ,"posiciones".center(25," ") )
            for i in db.arrayRows:
                if i.search == True:
                    if (len(i.position) == 0):
                        encontrado = "NO ENCONTRADO"
                    else:
                        encontrado = i.position
                    print(i.name.center(25," "),str(i.values).center(25," "),str(i.valueSearch).center(25," "),str(encontrado).center(25," "))
            print("\n")
            print("-------------------------------------------Fin de la lista-----------------------------------------------")
            print("\n")
            aaaa = input("Presiona enter para continuar: ")

    #--------------------------option list complete--------------------------
    if option ==4:
        if dataComplete == False:
            print("Aun no has cargado datos para desplegar las listas\n")
            aaaa = input("Presiona enter para continuar: ")

        elif dataComplete == True:
            os.system('clear')
            print("-------------------------------------lista total de operaciones registradas--------------------------------------\n")
            print("Nombre".center(15," "), "Valores".center(20," "), "Ordenar".center(10," "), "Datos ordenados".center(25," "), "Buscar".center(15," ") ,"Valor de busqueda".center(15," ") ,"Posiciones".center(15," ") )
            for i in db.arrayRows:
                # validate if exist search
                if i.search == True:
                    valorABuscar = i.valueSearch
                    if (len(i.position) == 0):
                        encontrado = "NO ENCONTRADO"
                    else:
                        encontrado = i.position
                else:
                    encontrado = "NO APLICA"
                    valorABuscar = "NO APLICA"

                # validate if exist sort
                if i.sort == True:
                    datosOrdenados = i.orderedValues
                else:
                    datosOrdenados = "NO APLICA"

                print(i.name.center(15," "),str(i.values).center(20," "),str(i.sort).center(10," "),str(datosOrdenados).center(25," "),str(i.search).center(15," "),str(valorABuscar).center(15," "),str(encontrado).center(25," "))
            
            print("\n")
            print("-------------------------------------------Fin de la lista-----------------------------------------------")
            print("\n")
            aaaa = input("Presiona enter para continuar: ")

'''
    if option==4: 
        outMenu=True
        print("Hasta Luego...")
'''
'''
    #option get out
    if option==6: 
        outMenu=True
        print("Hasta Luego...")
'''