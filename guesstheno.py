
rand=18 #our random number 
no_of_guess=0 #let say the no of guess is 0 in the starting 
while(no_of_guess<=5):
    print("enter any  number from 1 to 100 ")
    guessed_number=int(input())
    if guessed_number<rand:
        print("the number you have entered is smaller , so please enter a larger number ")
    elif guessed_number>rand:
        print("the number you have guessed is larger , so please enter a smaller number ")
    else:
        print("you have guessed the number correctly ")
        print("YOU WON ")
        print("you have guess the number in no_of_guess",)
        break
    print(no_of_guess,"no of guess left ")
    no_of_guess=no_of_guess+1
    if no_of_guess>5:
        print("game over ")
    