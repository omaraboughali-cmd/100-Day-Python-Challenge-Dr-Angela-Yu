choice1 = input("welcome to the treasure hunt"
                " you've arrived at a cross road"
                " choose direction ")
if choice1 == "right":
    choice2 = input("you've come to a lake"
                    " there is an island in the middle of"
                    " type wait to wait for a boat"
                    " type swim to swim through " )
    if choice2 == "wait":
        choice3 = input("you arrive at the island unharmed"
                        " there is a house with three doors one red"
                        " one yellow"
                        " and one blue"
                        " which color do you choose ")
        if choice3 == "blue":
            print ("you've found the treasue you win")
        else:
            print ("its a room full of fire game over")    
    else:
        print("game over")    
        
else:
    print("you fell into hole game over")