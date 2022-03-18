##Busca números primos##
n = int(input("ingrese numero: "))
i = 2
l = 1
cont = 0
for i in range(i,n+1):
    #print("###VALOR de i: " + str(i))
    l = i
    c = 0
    for l in range(i,0,-1):
        if i%l == 0:
            c += 1
        #print("--valor l: " + str(l))
        #print ("---i mod l = " + str(i%l))
        #print("----acumulado para " + str(i) + " es " + str(c))
        if l == 1 and c == 2:
            cont += 1
            print("..." + str(i) + " es PRIMO")
print("Se encontaron " + str(cont) + " números primos")

##Roger#Sandoval
