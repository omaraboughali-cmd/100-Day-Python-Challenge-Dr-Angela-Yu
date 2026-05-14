bids = {}
while True:
    name = input("what is your name")
    bid = input("what is your bid")
    another_bidder = input("is there another bidder")
    bids[name]=bid
    
    if another_bidder == "no":
        break
    print("\n"*100)
print(bids)
