'''7.Write a program which will allow user to enter 10 numbers and
display largest odd number from them. It will display appropriate
message in case if no odd number is found. '''

numbers = []
for i in range(10):
    num=int(input("Enter Number:-"))
    if num%2 !=0 :
        numbers.append(num)
print("Max Odd Is",max(numbers))


# Enter Number:-53
# Enter Number:-10
# Enter Number:-3
# Enter Number:-4
# Enter Number:-3
# Enter Number:-2
# Enter Number:-3
# Enter Number:-4
# Enter Number:-5
# Enter Number:-6
# Max Odd Is 53