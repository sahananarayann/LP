'''rock-->paper = paper wins
  rock--->scissors = rock wins
  paper--->scissors = scissor wins
  1 for rock 
  2 for paper 
  3 for scissor '''

import random

user_wins=0   #intializing to 0
computer_wins=0

options=["rock","paper","scissor"]

while True:
    user_input=input("rock\paper\scissor or Q to quit: ").lower() 
    if user_input=="q":
        break
    if user_input not in options:
        continue


    random_num=random.randint(0,2)
    #rock=0, paper=1, scissor=3
    computer_pick=options[random_num]
    print("computer picked", computer_pick,"-")
    

    if user_input=="rock" and computer_pick== "scissors":
        print("you won...!")
        user_wins+=1
        
    elif user_input=="paper" and computer_pick== "rock":
        print("you won...!")
        user_wins+=1

    elif user_input=="scissor" and computer_pick== "paper":
        print("you won...!")
        user_wins+=1

    else:
        print("you lost...!")
        computer_wins+=1


print("you won",user_wins,"times")
print("you lost",computer_wins,"times")
print("thank you for playing")







