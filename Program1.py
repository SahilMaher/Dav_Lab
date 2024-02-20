val1=int(input("Enter Your First value"))
val2=int(input("Enter Your Second Value"))
op=input("Which Operation do \n 1.addition \n 2.Subtraction \n 3.Multiplication \n 4.division \n Enter Number for your operation:-")


def add():
    print("Addition is",val1+val2)
def sub():
      print("Subtraction  is",val1-val2)
def mul():
         print("Multiplication  is",val1*val2)
def div():
         print("divition is",val1/val2)
if op=="1":
    add()
elif op=="2":
    sub()
elif op=="3":
    mul()
elif op=="4":
    div()
else:
    print("Enter valid number 1 to 5")