#import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen = turtle.Screen()
# my_screen.exitonclick()


# from prettytable import PrettyTable

# table = PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])
# table.add_column("Pokemon",["First","Second","Third","Fourth","Fifth","Sixths","Seventh"])

# table.align = "l"

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_menu = Menu()
new_coffee = CoffeeMaker()
want_coffee = True

while want_coffee:
    # Prints remaining ingredients
    new_coffee.report()
    try:
        drink = new_menu.find_drink(input(f"What kind of drink you want? We have: {new_menu.get_items()}.").lower())
    except:
        drink = new_menu.find_drink(input(f"What kind of drink you want? We have: {new_menu.get_items()}.").lower())
    # Error handling is missing if drink does not exist
    if new_coffee.is_resource_sufficient(drink):
        new_coffee.make_coffee(drink)
    else:
        want_coffee = False