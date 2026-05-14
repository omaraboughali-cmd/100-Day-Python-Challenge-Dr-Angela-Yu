import random

# A standard deck has 4 of every value (2-9), and 16 cards worth 10 (10, J, Q, K), plus 4 Aces.
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(deck) # Mix them up!
player_hand = []
dealer_hand = []
player_hand.append(deck.pop())
player_hand.append(deck.pop())
print(player_hand)
dealer_hand.append(deck.pop())
print(dealer_hand)
dealer_hand.append(deck.pop())
while sum(player_hand) < 21:
    choice = input("want to hit or stand")
    if choice == "H":
        player_hand.append(deck.pop())
        print(f'new hand = {player_hand} and total = {sum(player_hand)}')
        if sum(player_hand) > 21:
            print("game over")
            break
    else:
        print(dealer_hand)
        break

while sum(dealer_hand) < 17:
    dealer_hand.append(deck.pop())
    print(dealer_hand)


if sum(player_hand) > sum(dealer_hand) and sum(player_hand) <= 21 :
    print("you win")
elif sum(player_hand) == sum(dealer_hand):
    print("DRAW")
else:
    print("ai wins")
print(sum(player_hand) ,sum(dealer_hand))    