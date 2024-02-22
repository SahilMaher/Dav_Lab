import Module.mu as m
import Module.fees as f
# from mu import *
#  from mu import mca

dep=input("Enter Department:-")
if dep=="mca":
    sems=int(input("Enter Semester:-"))
    typ=input("Enter Type \n 1.Regular \n 2.Remedial")
    m.mca(sems)
    f.mcafees(sems,typ)
elif dep=="bca":
    sems=int(input("Enter Semester:-"))
    typ=input("Enter Type 1.Regular \n 2.Remedial \n")
    m.bca(sems)
    f.bcafees(sems,typ)
elif dep=="foca":
   
    m.foca()
else:
    print("Enter Valid Department")
