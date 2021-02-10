import os 
import menu
import read
import db

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
            print("aqui iran las listar ordenadas")
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