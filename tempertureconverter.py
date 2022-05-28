def fahren(temp):
    return ((temp*9)/5)+32



temp=int(input("enter the temperture in celcius :"))
converted=fahren(temp)
print("the temperture in fahrentiet is ", +converted)