def sum(num):
    return num+sum(num-1)

num=int(input("enter the value of natural number"))
c=sum(num) 
print(c)