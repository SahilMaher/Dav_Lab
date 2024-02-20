'''write a pro to create list od product along with price  laptop=50 insert 5 record from user and print appropriatly.'''
total=int(input("enter total number"))
product=[]
price=[]
for i in range(total):
    name=input("enter product name ")
    product.append(name)
for i in range(total):
    pri=int(input("enter price "))
    price.append(pri)
for i in range (total):
    print(product[i],"=>",price[i])

