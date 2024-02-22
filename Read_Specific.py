
file = open('hello.txt') 


content = file.readlines() 


strnum=int(input("Enter Strarting Line For Print"))

endnum=int(input("Enter Ending Line For Print"))
print(content[strnum:endnum]) 
