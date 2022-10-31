h = int (input ("Entrez la hauteur"))
l = int (input("Entrez la longueur"))

for i in range(h):
    for j in range(l):
        if j == 0 or j == l - 1:
                
                print ( '|' , end = '')
        
        elif ( i == 0 or i == h - 1):
                print ( '-' , end = '')

        else:
                print ('', end =' ')
    print()