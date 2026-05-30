products = {}
while True:
   
    item = input("enter item")
    price = int(input("enter price"))
    products[item] = price
    another = input("do you wish for more")
    if another != "yes":
        break
for item, price in products.items():
    print(f"{item} : {price}")
sum = 0
for price in products.values():
    sum += price
if sum > 100:
    sum -= (1/10)*sum

print(f"total = ${sum}")
             
