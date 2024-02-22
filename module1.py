import mu
import fees as f
dep=input("Enter Department:-")
if dep=="mca":
    sems=int(input("Enter Semester:-"))
    typ=input("Enter Type \n 1.Regular \n 2.Remedial")
    mu.mca(sems)
    f.mcafees(sems,typ)
elif dep=="bca":
    sems=int(input("Enter Semester:-"))
    typ=input("Enter Type 1.Regular \n 2.Remedial \n")
    mu.bca(sems)
    f.bcafees(sems,typ)
elif dep=="foca":
   
    mu.foca()
else:
    print("Enter Valid Department")
