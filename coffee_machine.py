MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0

total = 0

def input_coins():
    dimes = 0.10*float(input("how many dimes ? "))
    nickels = 0.05*float(input("how many nickels ? "))
    pennies = 0.01*float(input("how many pennies ? "))
    quarters = 0.25*float(input("how many quarters ? "))
    total = dimes + nickels + pennies + quarters
    return total


def is_resource_sufficent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("not enough resources")
            return False
    return True    

def deduct_resources(order_ingredients):
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]

def total_order(order_cost , total):
    change = total - order_cost
    
    if order_cost > total:
        print("not enough money")
    elif order_cost < total:
        print(f"here is your change ${change:.2f}")    
        print(f"here is your {choice} ☕")
        deduct_resources(drink["ingredients"])
    else:
        print(f"here is your {choice} ☕")    
        deduct_resources(drink["ingredients"])
    

while True:    
    choice = input("what would you like to drink espresso latte cappuccino? ")
    if choice in MENU:
        print(choice)
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficent(drink["ingredients"]):
            total = input_coins()
            total_order(drink["cost"], total)
            profit += drink["cost"]
    elif choice == "report":
        print(f"water : {resources["water"]}ml")
        print(f"milk : {resources["milk"]}ml")
        print(f"coffee : {resources["coffee"]}ml")
        print(f"money : ${profit}")  
    elif choice == "off":
        break              
