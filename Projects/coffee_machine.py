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


# Function to check if machine has enough resources to make the asked drink
def check_resources(drink):
    """Takes drink type and checks if machine has sufficient resources. Returns the insufficient product otherwise"""
    required_resources = MENU[drink]['ingredients']
    water_required = required_resources['water']
    milk_required = required_resources['milk']
    coffee_required = required_resources['coffee']

    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    if water_available < water_required:
        return 'water'
    elif milk_available < milk_required:
        return 'milk'
    elif coffee_available < coffee_required:
        return 'coffee'
    else:
        return 'yes'


# Function to deduct resources from machine once a cup of coffee is made
def make_coffee(available_resources, coffee_type):
    """Deduct the required ingredients according to the specified drink"""
    left_water = available_resources['water'] - MENU[coffee_type]['ingredients']['water']
    left_milk = available_resources['milk'] - MENU[coffee_type]['ingredients']['milk']
    left_coffee = available_resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']

    left_resources = {"water": left_water, "milk": left_milk, "coffee": left_coffee}
    return left_resources


new_coffee = True
profit = 0

while new_coffee:
    # Prompt user for their choice
    choice = input("What would you like? (espresso/latte/cappuccino: ").lower()

    # Turn off the Coffee Machine by entering “off” to the prompt
    if choice == 'off':
        new_coffee = False

    # Print report if asked
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    # If choice is any three of these coffees, then move forward
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":

        # Check if resources are sufficient
        enough_resources = check_resources(choice)

        # In case of insufficient resources in coffee machine
        if enough_resources != 'yes':
            print(f"Sorry there is not enough {enough_resources}.")

        # If resources are sufficient, then move forward
        else:
            # Process coins
            print("Please insert coins.")

            total = float(input("how many quarters?: ")) * 0.25
            total += float(input("how many dimes?: ")) * 0.10
            total += float(input("how many nickels?: ")) * 0.05
            total += float(input("how many pennies?: ")) * 0.01

            # Required money to make selected drink
            money_required = MENU[choice]['cost']

            # Check transaction is successful or not
            if total < money_required:
                print("Sorry that's not enough money. Money refunded.")

            # If successful, then add given money to coffee machine and return extra money
            else:
                change = round(total - money_required, 2)
                profit += money_required
                print(f"Here is your ${change} change.")
                print(f"Here is your {choice} ☕. Enjoy!")

                # Make Coffee
                resources = make_coffee(resources, choice)

    # In case of invalid choice
    else:
        print("We don't offer that kind of coffee.")
