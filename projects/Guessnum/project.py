from random import randint

rannum  = randint(1,100)
count =0

while True:
  playernum = int(input("guess the number : "))
  count+=1
  if(playernum > rannum):
    print("Lower number please")
  elif(playernum < rannum):
    print("Higher number please")
  else:
    print(f"Guessed correctly and no of guesses you take : {count}") 
    break   
  