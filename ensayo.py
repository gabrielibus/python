def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                print("True")
            else:
                print("False")

superposicion ([1,2],[3,4])