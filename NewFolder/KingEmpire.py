def KingEmpire(m):
    """
    :param m: no of sections in the street
    :return: number of possible assignments
    """
    i=0
    for i in range(m):
        if m==1 :
            return 1
        else:
            a= m +(m-1)

    print("Output", a**2)

KingEmpire(3)
