import os 
import menu
import read


outMenu = False
while outMenu==False:
    os.system('clear')
    menu.menu()
    option =    int(input(">>>> "))
    
    #option cargar archivo
    if option==1:
        read.read()

    #option get out
    if option==6: 
        outMenu=True
        print("Hasta Luego...")