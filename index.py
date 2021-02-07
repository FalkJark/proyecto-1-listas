import os 
import menu

outMenu = False
while outMenu==False:
    os.system('clear')
    menu.menu()
    option =    int(input(">>>> "))
    if option==6: 
        outMenu=True
        print("Hasta Luego...")