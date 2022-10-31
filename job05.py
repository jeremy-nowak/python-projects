input1 = int (input ("entrez une premiere valeur"))
input2 = int (input ("entrez une deuxieme valeur"))
for i in range(input1+1, input2) or range(input1, input2-1):
    print(i)
if input1 == input2:
    print ("valeurs égale")