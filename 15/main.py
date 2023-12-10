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


def is_resource_sufficient():
    """Returns True when order can be made, False if ingredients are insufficient."""
    pass


def process_payment():
    """Returns the total payment received and issue change."""
    pass

def make_coffee():
    """Deduct the required ingredients from the resources."""
    pass


while True:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    break
