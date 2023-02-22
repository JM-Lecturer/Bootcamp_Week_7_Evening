def RunMenu(MenuItems):
    print(MenuItems[0])

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