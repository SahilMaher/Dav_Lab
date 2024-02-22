'''Write A program to take user input of 10 numbers and create odd and event list sepretly
check it out maximam numbers of odd list and even list'''
odd=[]
even=[]
for n in range(10):
    num=int(input("Enter Number"))
    if num%2==0:
        even.append(num)
    else: 
        odd.append(num)
print("Odd Numbers is:-",odd)
print("Even Numbers is:-",even)

if max(odd) > max(even):
    print("odd number is Max:-",max(odd))
else:
    print("Even is max",max(even))



