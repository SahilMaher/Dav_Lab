'''write a program to check given string has how many total number of vowels take String from uer'''
str=input("Enter String:-")
str_len=len(str)
e=0
i=0
a=0
u=0
o=0

for n in range(str_len):
    if str[n]=='a':
        a=a+1
    elif str[n]=='i':
        i=i+1
    elif str[n]=='o':
        o=o+1
    elif str[n]=='u':
        u=u+1
    elif str[n]=='e':
        e=e+1

print("a is:-",a,"\n e is :-",e,"\n i is:-",i,"\n o is",o,"\n u is:-",u)        
        


