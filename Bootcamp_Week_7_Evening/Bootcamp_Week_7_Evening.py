class Vehicle:
    colour = ""
    wheelsCount = 0
    maxSpeed = 0
    name = ""

    def __init__(self, colour, wheelCount, maxSpeed, name):
        self.colour = colour
        self.wheelsCount = wheelCount
        self.maxSpeed = maxSpeed
        self.name = name

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

Vehicles = list()
Vehicles.append(Vehicle("Red", 2, 10, "Bicycle"))
Vehicles.append(Vehicle("Yellow", 0, 40, "Submarine"))
Vehicles.append(Vehicle("Black", 4, 70, "Taxi"))
Vehicles.append(Vehicle("Green", 16, 50, "Tank"))
Vehicles.append(Vehicle("White", 3, 130, "Airplane"))

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