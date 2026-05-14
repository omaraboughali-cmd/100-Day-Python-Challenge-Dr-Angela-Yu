import random
word_list = ["baboon" , "camel" , "giraffe"]
word = random.choice(word_list)
print(word)
blanks ="_"*len(word)
print(blanks)
lives = 4
while lives > 0 and "_" in blanks :
    
        print(lives)
        guess = input("guess a letter")
        if guess in word:
            lives = lives
        else:
            lives -= 1    

        for i, letter in enumerate(word):
            if letter == guess:
                new_blanks = list(blanks)
                new_blanks[word.index(guess)] = guess
                        
                new_blanks[i] = guess
                blanks = "".join(new_blanks)

        print(blanks)    

