'''WAP to create a file using file handaling in python write three line into the file'''
file =open("hello.txt","w")
file.write("hello world! \n Good Morning \n Have a nice Day")
file.close()