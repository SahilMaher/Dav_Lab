'''Write a Program to create a list of products along with price i.e. laptop=50000,mobile=40000
insert 5 records from users and print apropriatly
'''
pro_num=int(input("Enter how many product Enter:-"))
products=[]
price=[]
for i in range(pro_num):
    pro_name=input("Enter Product name:-")
    products.append(pro_name)
    pro_prc=input("Enter Product Price:-")
    price.append(pro_prc)

j=0
while j<pro_num:
    print(products[j],"=",price[j])
    j=j+1

