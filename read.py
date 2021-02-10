import os
import db
#import index

def sortOnMyOwn(v):
    for i in range(len(v)-1):
        for j in range(len(v)-1):
            if v[j] > v[j+1]:
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux
    return v     

def read():
    nameFile = input("Ingresa la ruta de tu archivo: ")
    archivo = open(nameFile)
    lines = archivo.readlines()
    archivo.close()
    
    for i in lines:
        i = i.rstrip("\n")
    
        #catch the name
        tem = i.split("=")
        nameRow = tem[0].rstrip(" ") # <----------- indica el nombre de la lista

        #catch the operation sort
        sortRow = False
        if("ORDENAR" in tem[1]):
            sortRow = True # <----------------- indica si hay que hacer ordenamiento
            tem[1] = tem[1].replace("ORDENAR","")
            tem[1] = tem[1].rstrip(" ")
            tem[1] = tem[1].rstrip(",")


        #catch the operation search
        searchRow = False
        valueSearchRow = None
        if("BUSCAR" in tem[1]):
            searchRow = True # <--------------- indica si hay que realizar una busqueda
            tem[1] = tem[1].replace("BUSCAR","")
            l = tem[1].rstrip(" ")
            l = (len(tem[1]))
            valueSearchRow = tem[1][l-1] # <---------- indica que valor debemos buscar
            tem[1] = tem[1].rstrip(str(valueSearchRow))
            tem[1] = tem[1].rstrip(" ")
            tem[1] = tem[1].rstrip(",")

        #catch the values
        valuesTemp = tem[1].split(",")
        valuesRow = []   # <---------- lista con los valores
        for j in valuesTemp:
            aux = int(j.strip())
            valuesRow.append(aux)
        
        
        #---------------------------------------- SEARCH --------------------------------------------
        positionRow = []
        if searchRow == True:
            cont = 1
            for n in valuesRow:
                #print("valores: ",n)
                #print("valor de busqueda: ",valueSearchRow)
                if int(n) == int(valueSearchRow):
                    positionRow.append(cont)
                cont = cont + 1  

        #add to vector rows all the information
        fila = db.row(nameRow,valuesRow,sortRow,searchRow,valueSearchRow,positionRow)
        db.arrayRows.append(fila)


    #fuera del for
    for i in db.arrayRows:
        if i.sort == True:
            vd = i.values.copy()
            vo = sortOnMyOwn(vd)
            i.orderedValues = vo

    os.system('clear')
    print("\n")
    print("-------------------------------------Datos cargados con exito-------------------------------------\n")
    
    aaaa = input("Presiona enter para continuar: ")


        


    '''
        #segmento de prueba
        print("nombre de la lista: ",nameRow)
        print("ordenar: ",sortRow)
        print("buscar: ",searchRow)
        if searchRow==True: 
            print("Numero a buscar: ",valueSearchRow)
        print("valore de la lista: ",valuesRow)
        print("\n")

    '''
