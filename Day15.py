#excercise 1: Coffee machine project

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
    "coffee":100,
    "money":0
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: Rs.{resources['money']}")

def resource_sufficient(water,milk,coffee):
    if resources['water'] >= water:
        if resources["milk"] >= milk:
            if resources["coffee"] >= coffee:
                return True
            else:
                return "Coffee"
        else:
            return "Milk"
    else:
        return "Water"  

def cash_transaction(money):
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))   
    dimes = int(input("How many dimes?: ")) 
    nickles = int(input("How many nickles?: ")) 
    pennies = int(input("How many pennies?: "))    
    total_in_penny = quarter*25 + dimes*10 + nickles*5 + pennies
    total = total_in_penny/100   
    if total == money:
        resources['money'] += money
        return True
    elif total > money:
        resources['money'] += money
        return total-money
    else:
        return False

def choice(type):
    if type == "espresso":
        water = 50
        milk = 0
        coffee = 18
        money = 1.50
    elif type == "latte":
        water = 200
        milk = 150
        coffee = 24
        money = 2.50
    elif type == "cappuccino":
        water = 50
        milk = 150
        coffee = 18
        money = 3.00
    else:
        print("Invalid Input.")    
    result = resource_sufficient(water,milk,coffee)
    if result is True:
        cash = cash_transaction(money) 
        if cash is True or cash != 0:
            resources["water"] = resources['water'] - water
            resources["milk"]  = resources['milk'] - milk
            resources["coffee"] = resources['coffee'] -coffee 
            if cash != 0:
                print(f"Here is Rs.{cash} in change.") 
            print(f"Here is your {type}. Enjoy!") 
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Sorry there is not enough {result}.")

off = False
money = 0
while not off:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_coffee == "off":
        off = True
    elif user_coffee == "report":
        report()
    else:
        choice(user_coffee)

