import random

def game():
    print("You are playing a game")
    score = random.randint(1,80)

    f = open("Hi-score.txt","r")
    highsc = f.read()
    if(highsc == ""):
        highsc = 0
    else:
        highsc = int(highsc)
    print(f"your score is : {score}")
    if(score > highsc):
      f1 = open("Hi-score.txt","w")
      f1.write(str(score))

game()    