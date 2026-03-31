

import random

'''
snake - 1
water - 0
gun - -1
'''
computer = random.choice([-1,0,1])

urchoice = input("Your choice: ")
dict = {"s" : 1,"w":0,"g":-1}
urnum = dict[urchoice]

reversedict= {1:"snake",0:"water",-1:"gun"}
print(f"Your choice is : {reversedict[urnum]} \nComputer choice is : {reversedict[computer]}")

if(computer == urnum):
    print("Its a draw")
else:
    if(urnum == 1 and computer == 0):
        print("you win")
    elif(urnum == 1 and computer == -1):
        print("you loose")  
    elif(urnum == 0 and computer == -1):
        print("you win") 
    elif(urnum == 0 and computer == 1):
        print("you loose") 
    elif(urnum == -1 and computer == 1):
        print("you win") 
    elif(urnum == -1 and computer == 0):
        print("you loose")    
    else: 
        print("Something went wrong")
        
        