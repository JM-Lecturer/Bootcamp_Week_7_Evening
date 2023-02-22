class Vehicles:
    colour = ""
    wheelsCount = 0
    maxSpeed = 0
    name = ""

    def __init__(self):
        self.colour = "Red"
        self.wheelsCount = 2
        self.maxSpeed = 10
        self.name = "Bicycle"

def RunMenu(MenuItems):
    print(MenuItems[0])

    for i in range(1, len(MenuItems)):
        print(str(i) + ": " + MenuItems[i])


MenuItems = list()
MenuItems.append("----------Menu----------\n\n")
MenuItems.append("View Stock")
MenuItems.append("Purchase Items")
MenuItems.append("Exit")
RunMenu(MenuItems)