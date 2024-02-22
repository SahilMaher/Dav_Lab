''' create one module name of mu in which create three diffrent function  
1. mca semester, and subject
 2.bca 
 3.foca full form and courses
 
 import this module and use this module into some other python program and call all function and print the out put 
 generate five diffrent out put '''

def mca(sem):
    if sem==1:
        print("RDBMS")
        print("Java")
        print("OS")
        print("DS")
    elif sem==2:
        print("python")
        print("DAV")
        print("Android")
        print("Networking")
    else:
        print("Enter Valid Samester Like 1 or 2")
def bca(sem):
    if sem==1:
        print("C")
        print("HTML")
        print("JAVASCRIPT")
        print("CS")
    elif sem==2:
        print("NETWORKING")
        print("C++")
        print("PHP")
        print("WORDPRESS")
    else:
        print("Enter Valid Samester Like 1 or 2")
def foca(cours):
    print("Faculty of Computer Application")
    print("1.MCA\n2.BCA \n 3.MCs \n Enter Any Course Name:-")
    if cours=="mca":
        print("In Mca Available 2 Semester \n Fees is 50000")
    elif cours=="bca":
        print("In Bca Available 6 Semester \n Fees is 20000")
    elif cours=="msc":
        print("mcs have Two types \n 1.Cyber 2.Data Science")
    else:
        print("course is not available")    
