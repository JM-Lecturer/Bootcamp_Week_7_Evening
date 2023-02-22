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
    #Add in validation for the users input!
    for i in range(1, len(MenuItems)):
        print(str(i) + ": " + MenuItems[i])

    choice = int(input("\nPlease select from the options above\n"))
    return choice


MenuItems = list()
MenuItems.append("----------Menu----------\n")
MenuItems.append("View Stock")
MenuItems.append("Purchase Items")
MenuItems.append("Exit")

loop = True
while loop == True:

    choice = RunMenu(MenuItems)

    if choice == 1:
        print("View coming soon...")
    elif choice == 2:
        print("Purchasing coming soon...\n")
    else:
        print("\nGoodbye")
        loop = False