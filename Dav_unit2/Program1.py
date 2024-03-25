'''1. Write a program to create a list of names; then define a function
to display all the elements in the received list. Call the function to
execute its statements and display all names in the list.'''

names=[]
num=int(input("Number OF Elements in list"))
for i in range(num):
     name=input("Enter Name:-")
     names.append(name)

def display():
  
    print(names)



   
display()

#out put
# Number OF Elements in list3
# Enter Name:-ram
# Enter Name:-shita
# Enter Name:-laxman
# ['ram', 'shita', 'laxman']
