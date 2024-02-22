'''WAP to append a file that you have created in program one with appending one line '''
file=open("hello.txt","a")
file.write("DAV is Subject in Mca 2")
file.close()
file=open("hello.txt","r")
data=file.read()
print(data)
