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


def is_resource_sufficient(selected_menu: str) -> bool:
    """Returns True when order can be made, False if ingredients are insufficient."""
    ingredients = ['water','milk','coffee']
    for ingredient in ingredients:
        if ingredient in MENU[selected_menu]['ingredients'] and MENU[selected_menu]['ingredients'][ingredient] > resources[ingredient]:
            print(f"insufficient {ingredient}, remaining: {resources[ingredient]}, required for {selected_menu}: {MENU[selected_menu]['ingredients'][ingredient]}")
            return False
    return True

def process_payment() -> float:
    """Returns the total payment received and issue change."""
    payment = 0.0
    price = MENU[selected_menu]['cost']
    while payment < price:
        print(f"Price for {selected_menu}: {price}. You paid {payment}. Remaining: {price - payment}")
        payment += float(input("​Make payment\n"))
    return payment - price

def make_coffee(selected_menu: str):
    """Deduct the required ingredients from the resources."""
    ingredients = ['water','milk','coffee']
    for ingredient in ingredients:
        if ingredient in MENU[selected_menu]['ingredients']:
            resources[ingredient] -= MENU[selected_menu]['ingredients'][ingredient]


while True:
    print(f"\nAdmin View")
    print(f"Profit: {profit}")
    print(f"Menu: {MENU}")
    print(f"resources: {resources}\n")
    print("Menu Options: ")
    print(f"0 -> Espresso: {MENU['espresso']['cost']}")
    print(f"1 -> Latte: {MENU['latte']['cost']}")
    print(f"2 -> Cappuccino: {MENU['cappuccino']['cost']}")
    choice = int(input("​What would you like? (0: espresso / 1: latte/ 2: cappuccino): \n"))
    selected_menu = ""
    match choice:
        case 0:
            selected_menu = 'espresso'
        case 1:
            selected_menu = 'latte'
        case 2:
            selected_menu = 'cappuccino'
        case _:
            print("Invalid menu choice, click enter to continue")
    can_make = is_resource_sufficient(selected_menu)
    if not can_make:
        print("Resource insufficient, click enter to continue")
        continue
    change = process_payment()
    make_coffee(selected_menu)

    profit += MENU[selected_menu]['cost']
    print(f"Change issued: {change}")
    print(f"Profit added: {MENU[selected_menu]['cost']}, total profit: {profit}")
    print("Click enter to continue")

