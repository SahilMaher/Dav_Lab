def feebca():
    s=input(print("enter 1 for (regural) and enter 2 for (repat)"))
    s=int(s)
    if s == 1:
        sem =input("Enter Your Semester \n( 1,2,3,4,5,6)\n")
        sem=int(sem)
        if  sem>0:
            print ("B.C.A. semester ",sem, "fees = 45,000")
    elif s==0:
        rsem=input("Enter Your Semester \n( 1,2,3,4,5,6)\n")
        rsem=int(rsem)
        if  rsem>0:
            print ("B.C.A. semester ",rsem, "fees = 45,000")

feebca()
