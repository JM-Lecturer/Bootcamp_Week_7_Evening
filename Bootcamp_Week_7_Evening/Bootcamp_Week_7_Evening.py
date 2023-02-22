class Vehicle:
    colour = ""
    wheelsCount = 0
    maxSpeed = 0
    name = ""
    stock = 0

    def __init__(self, colour, wheelCount, maxSpeed, name, stock):
        self.colour = colour
        self.wheelsCount = wheelCount
        self.maxSpeed = maxSpeed
        self.name = name
        self.stock = stock

def RunMenu(MenuItems):
    print(MenuItems[0])
    #Add in validation for the users input!
    for i in range(1, len(MenuItems)):
        print(str(i) + ": " + MenuItems[i])

    choice = int(input("\nPlease select from the options above\n"))
    return choice

def DisplayVehicles(Vehicles, stock):
    print("----------Vehicles----------\n")

    for i in range(0, len(Vehicles)):
        print("Vehicle " + str(i + 1) + "\n Name: " + Vehicles[i].name + "\n Colour: " + Vehicles[i].colour + "\n Wheels: " + str(Vehicles[i].wheelsCount) + "\n Max Speed: " + str(Vehicles[i].maxSpeed))
        if stock == True:
            print(" Stock: " + str(Vehicles[i].stock))
        print("")

def AddVehicles(Vehicles):
    
    loop = True
    while loop == True:
    
        DisplayVehicles(Vehicles, False)

        MenuItems = list()
        MenuItems.append("Options:\n")
        MenuItems.append("Add Item")
        MenuItems.append("Exit")

        choice = RunMenu(MenuItems)

        if choice == 1:
            print()
        else:
            loop = False

def PurchaseVehicles(Vehicles):
    #Remove any vehicles from the options where the stock is 0
    loop = True
    while loop == True:

        DisplayVehicles(Vehicles, True)

        MenuItems = list() 
        MenuItems.append("Which vehicle would you like to buy:")

        for i in range(0, len(Vehicles)):
            MenuItems.append(Vehicles[i].name)

        MenuItems.append("Exit")

        choice = RunMenu(MenuItems)

        if choice == len(MenuItems) - 1:
            loop = False
            print("\n\n")
        else:
            Vehicles[choice - 1].stock = Vehicles[choice - 1].stock - 1

#-------------------------------------------------------------------------------------------------------

MenuItems = list()
MenuItems.append("----------Menu----------\n")
MenuItems.append("View Stock")
MenuItems.append("Purchase Items")
MenuItems.append("Add Items")
MenuItems.append("Exit")

Vehicles = list()
Vehicles.append(Vehicle("Red", 2, 10, "Bicycle", 200))
Vehicles.append(Vehicle("Yellow", 0, 40, "Submarine", 1))
Vehicles.append(Vehicle("Black", 4, 70, "Taxi", 12))
Vehicles.append(Vehicle("Green", 16, 50, "Tank", 2))
Vehicles.append(Vehicle("White", 3, 130, "Airplane", 3))

loop = True
while loop == True:

    choice = RunMenu(MenuItems)

    if choice == 1:
        DisplayVehicles(Vehicles, False)
    elif choice == 2:
        PurchaseVehicles(Vehicles)
    elif choice == 3:
        AddVehicles(Vehicles)
    else:
        print("\nGoodbye")
        loop = False