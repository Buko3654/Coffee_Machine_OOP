from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
mr_coffee = CoffeeMaker()
common_cents = MoneyMachine()
menu = Menu()

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        mr_coffee.report()
        common_cents.report()
    else:
        drink = menu.find_drink(order)
        if mr_coffee.is_resource_sufficient(drink):
            if common_cents.make_payment(drink.cost):
                mr_coffee.make_coffee(drink)
