'''wap to use r+ and w+ mode with appropriate example and comments'''
#in r+ mode the cursor is write data on end of old content that not override data
file=open("hello.txt","r+")
data =file.read()
print(data)
file.write("hello how are you \n good morning \n This is mca 2")
print(data)
