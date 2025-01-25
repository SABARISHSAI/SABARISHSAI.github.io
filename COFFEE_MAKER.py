MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
accounts = 0


def available_check(order):
    for i,j in zip(MENU[order]['ingredients'],resources):
            if MENU[order]['ingredients'][i] > resources[j]:
                return False,j,
    return True,True
def make_order(order):
    for i, j in zip(MENU[order]['ingredients'], resources):
        resources[j]= resources[j]-MENU[order]['ingredients'][i]
    print(f"Here is your {order} . Enjoy!")
def pay_order(order):
    print("please insert coins")
    cost = MENU[order]['cost']
    quarters_mul = 0.25
    dimes_mul = 0.10
    nickles_mul =0.05
    pennies_mul = 0.01
    quarters = int(input("how many quarters : ")) * quarters_mul
    dimes = int(input("how many dimes : ")) * dimes_mul
    nickles = int(input("how many nickles : ")) * nickles_mul
    pennies = int(input("how many pennies : ")) * pennies_mul
    total_user_give = quarters+dimes+nickles+pennies
    if total_user_give>cost:
        print(f"here is the change {round(total_user_give-cost,2)}")
        return True
    else:
        return False

get_order = True
account = 0
while get_order:
    order = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if order == 'report':
        for i in resources:
            print(f'{i}:{resources[i]}')
    if order == 'off':
        get_order = False
        print("SHUTTING OFF!!!")
    if order != 'report' and order !='off' and order != 'account':
        check,balance = available_check(order)
        if check == False and balance!=True:
            print(f"Sorry there is not enough {balance}, Try order something else")
        else:
            if pay_order(order):
                make_order(order)
                account += MENU[order]['cost']
            else:
                print(f"insufficient money to make order try adding more money")
    if order=='account':
        print(f"the business so far happened is {account}")

