def Fonction (*parametre):
    MyList = []
    for param in parametre:
        if isinstance(param, (int)):
            MyList.append(param)
    for element in MyList:
        if element %2 == 0:
            print (element)

Fonction(3,5,4,8,43,6,24)
