import random
str1=int(input("Enter Startint values"))
end1=int(input("Enter Ending values"))
if str1 == end1:
    print("Enter valid value")
elif end1 < str1 :
    print("Enter Bigger Values last")

else:
    num=random.randrange(str1,end1)
    print(num)