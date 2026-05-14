import random
rock = print("rock")
paper = print("paper")
scissor = print("scissor")

game = ["rock","paper","scissor"]
player1 = input("choose rock paper scissor")
player2 = game[random.randint(0,2)]
if player1 == player2:
    print("draw") 
elif player1 == "rock" and player2 == "scissor" or player1 == "scissor" and player2 == "paper" or player1 == "paper" and player2 == "rock":
    print("you win")
elif player1 == "paper" and player2 == "scissor" or player1 == "scissor" and player2 == "rock" or player1 == "rock" and player2 == "paper":
    print ("computer wins")      

student_scores = [20, 30, 40]
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)    