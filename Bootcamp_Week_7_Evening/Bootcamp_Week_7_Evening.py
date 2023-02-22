def RunMenu(MenuItems):
    print(MenuItems[0])
    #ItemsCount = MenuItems.count

    for i in range(1, len(MenuItems)):
        print(str(i) + ": " + MenuItems[i])


MenuItems = list()
MenuItems.append("----------Menu----------\n\n")
MenuItems.append("View Stock")
MenuItems.append("Purchase Items")
MenuItems.append("Exit")
RunMenu(MenuItems)