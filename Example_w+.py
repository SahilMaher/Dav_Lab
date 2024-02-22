'''wap to use r+ and w+ mode with appropriate example and comments'''
#file cursor is Strart on the beagining and remove old content and write new
file=open("hello.txt","w+")
file.write("hello how are you \n good morning")
file.seek(0)
data=file.read()
print(data)
