'''Write a program to take user input for the list of 
number and you have to create list of squaer of even numbers and cube of odd number '''

num=int(input("Enter How Many Value Enter:-"))
even=[]
odd=[]
for n in range(num):
    val=int(input("Enter Value:-"))
    if val%2==0:
        even.append(val*val)
    else:
        odd.append(val*val*val)
print(even)
print(odd)
