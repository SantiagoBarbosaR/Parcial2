def elemntosRepetidos():

    l1 = ("A","B","C","D","E")
    l2 = ("A","B","A","C","A")

  
    
    for i in  range (len(l1)):
        (l1.count(l1[i]))
        
    if (l1.count(l1[i])) > 1:
        print ("HAY ELEMTOS REPETIDOS EN L1")
    else:
        print("NO HAY ELEMTOS REPETIDOS EN L1")

    for i in  range (len(l2)):
        (l2.count(l2[i]))

    if (l2.count(l2[i])) > 1:
        print ("HAY ELEMTOS REPETIDOS EN L2")
    else:
        print("NO HAY ELEMTOS REPETIDOS EN L2")


    


def CadenaEnLista():
    s = ("p","r","o","g","r","a","m","a","c","i","o","n")
    c = "cion"
    d = ""
    e = "sapo"
    
    for i in range (len(s)):

        d = d +(s[i])

    if c  in d:

        print (s)

    else:
        print("no exixte")
    
    if e  in d:

        print (s)

    else:
        print("no exixte sapo en la oracion")


def promedio():
    a = [6.2,20,10,568,6.5,3.33]
    
    for i in range (len(a)):
        b = 0
        b = b +(a[i])
        c = b/(len(a))
    
    print(c)

promedio()