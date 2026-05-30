import random
print("welcome to guess the number")
print("im thinking of a number between 1 and 100")
difficulty = input("choose a difficulty easy med high ")
if difficulty == "easy":
    lives = 9
elif difficulty == "med":
    lives = 5
elif difficulty == "high":
    lives = 3
else:
    print("invalid input")
guessed_num = random.randint(1,100)
#print(guessed_num)
while lives >= 1:
    guess_num = int(input("guess number "))
    if guess_num == guessed_num:
        print("correct")
        break
    elif guess_num == guessed_num + 1 or guess_num == guessed_num - 1:
        print("so close + or - 1")           
        lives -= 1
        print(f"remaining lives {lives}")
    elif guess_num > guessed_num:
        print("too high")
        lives -= 1
        print(f"remaining lives {lives}")
    elif guess_num < guessed_num:
        print("too low")
        lives -= 1
        print(f"remaining lives {lives}")

if lives == 0:
    print("gameover")        
    
