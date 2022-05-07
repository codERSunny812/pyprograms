# print("this calculator is  made by sunny !!!! \n just for fun in which you will didn't get the right answer of some specified problem  ")
def calculator():
 print("please select any of the operator given below \n 1. '+' \n 2. '-' \n 3.'*'\n 4.'/' \n 5. '%' \n" )
#  op= int(input())
op=input("enter the operator \n")
print("enter the first number \n")
num1=int(input())
print("enter the second number \n")
num2=int(input())
if op == "+":
    if num1 == 56 and num2 == 9:
        print("the sum of the number is ",77)
    else:
        print("Sum is:",num1 + num2)
if op == "-":
    print("Substract is:",num1-num2)
if op== "*":
    if num1 == 45 and num2 == 3:
        print("the multiplication of the number is :",555)
    else:
        print("Multiply is :",num1*num2)
if op == "/":
    if num1 ==56 and num2 == 6:
        print("4")
    else:
        print("Divide is:",float(num1/num2))
        
        
        def repeat():
            print("press y to calculate again and n to exit :")
            choice=input()
            if choice=='y':
                calculator()
            else:
                print("thank you for using my calculator ")
            
            
         