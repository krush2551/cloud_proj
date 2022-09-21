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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not sufficient {item} ")
            return False
    return True

def process_coins():
    print("Please insert coins")
    total= int(input("how many quarters? : "))*0.25
    total+= int(input("how many dimes?: "))*0.1
    total += int(input("how many nickel?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received>=drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+= drink_cost
        return  True
    else:
        print("sorry not enough money")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} . Enjoy!")
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_on= False
    elif choice == "report":
        print(f"water :{resources['water']}")
        print(f"water :{resources['milk']}")
        print(f"water :{resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
# done = False
# def report():
#
#         resources["water"] -=  MENU[choice]["ingredients"]["water"]
#         resources["milk"] -=  MENU[choice]["ingredients"]["milk"]
#         resources["coffee"] -=  MENU[choice]["ingredients"]["coffee"]
#         print(f'water: {resources["water"]}, coffee: {resources["coffee"]},milk: {resources["milk"]}')
# def check():
#     water_left = resources["water"] - MENU[choice]["ingredients"]["water"]
#     coffee_left =  resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
#     milk_left = resources["milk"] - MENU[choice]["ingredients"]["milk"]
#     if water_left > MENU[choice]["ingredients"]["water"] or coffee_left >MENU[choice]["ingredients"][
#         "coffee"] or milk_left > MENU[choice]["ingredients"]["milk"]:
#         check_coins()
#
#     else:
#         print("Sorry there is not enough ingredients")
#         done=False
# def check_for_espresso():
#     water_left = resources["water"] - MENU[choice]["ingredients"]["water"]
#     coffee_left = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
#
#     if water_left > MENU[choice]["ingredients"]["water"] or coffee_left > MENU[choice]["ingredients"][
#         "coffee"] :
#         check_coins()
#
#     else:
#         print("not sufficient")
#         done = False
#
# def check_coins():
#     print("Please insert coins")
#     quarter = int(input("insert quarters?"))
#     dimes = int(input("insert dimes?"))
#     nickles = int(input("insert nickles?"))
#     pennies = int(input("insert pennies?"))
#     money_required =  0.25*quarter + 0.10*dimes + 0.05* nickles+ 0.01*pennies
#     print(f"money required = {money_required}")
#     if money_required == MENU[choice]["cost"]:
#         print("here's your coffee")
#     elif money_required > MENU[choice]["cost"]:
#         return_cost = MENU[choice]["cost"] - money_required
#         print(f"here's the money left {return_cost}")
#         print("Please enjoy")
#     else:
#         print("Not enough money")
# while not done:
#
#     choice = input("What would you like?  (espresso/latte/cappuccino): ")
#
#
#     if choice=="report":
#          report()
#
#
#     elif choice == "latte" or choice=="cappuccino":
#
#         check()
#
#
#     elif choice=="espresso":
#
#         check_for_espresso()
#
#     elif choice=="off":
#         done=False
#
