'''8. Write a Python program to perform following operation on given
string input:
a) Count Number of Vowel in given string
b) Count Length of string (do not use Len ())
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not '''

str1=input("Enter Your String:-")

def Vowel():
    a=str1.count('a')
    e=str1.count('e')
    i=str1.count('i')
    o=str1.count('o')
    u=str1.count('u')
    print("e is:-",e," Times")
    print("a is:-",a," Times")
    print("i is:-",i," Times")
    print("o is:-",o," Times")
    print("u is:-",u," Times")
    print("There Are ",e+a+i+u+o,"Vowels in above String")
def lenstr():
    count=0
    for i in str1:
        count=count+1
    print("The Length of String is:-",count)
def revstr():
    strrev=str1[::-1]
    print(strrev)

def strreplace():
    repstr=input("Enter String Do you Want to Replace:-")
    newstr=input("Enter New String:- ")
    finslstr=str1.replace(repstr,newstr)
    print(finslstr)

def palistr():
     strrev=str1[::-1]
     if strrev==str1:
        print("String is Palindrome")
    else:
        print("String Is not Palindrome")

Vowel()
lenstr()
strreplace()
revstr()
palistr()