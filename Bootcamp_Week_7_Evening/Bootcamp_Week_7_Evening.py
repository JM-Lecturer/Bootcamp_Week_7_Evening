def RunMenu(MenuItems):
    print(MenuItems[0])
    #ItemsCount = MenuItems.count

    for i in range(1, len(MenuItems)):
        print(str(i) + ": " + MenuItems[i])


print("----------Static Menu----------\n\n")
print("1: Start")
print("2: Section 2")
print("3: Exit")

MenuItems = list()
MenuItems.append("----------Dynamic Menu----------\n\n")
MenuItems.append("View Stock")
MenuItems.append("Purchase Items")
MenuItems.append("Exit")
RunMenu(MenuItems)