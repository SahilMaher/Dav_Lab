'''write a program to create udf studentData() print name,age,city by calling udf with all four types of perametrt
(all two and defualt )
'''
#default
def studentData(name,age=20,city="porbandar"):
    print("Name Is:-",name)
    print("Age Is:-",age)
    print("City Is:-",city)
studentData("Bhagat")
#keyword Argument
print(studentData(name="sahil",age=21,city="porbandar"))