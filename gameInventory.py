# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    values = []
    for i in inventory:
        values.append(inventory[i])
        print(inventory[i], i)

    print("Total number of items:", sum(values))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    longest = max(inventory, key=len)
    longest = len(longest)
    longest = max(longest, 10)
    formatstr = '{:>' + str(longest) + '}' + '{:>' + str(longest) + '}'
    print("Inventory:")
    print(formatstr.format('count', 'item name'))
    print(2 * int(longest) * "-")
    values = []

    if order is None or order == "":
        for i in inventory:
            values.append(inventory[i])
            print(formatstr.format(inventory[i], i))

    elif order == "count,desc":
        copyinv = dict(inventory)
        while len(copyinv) > 0:
            maximum = max(copyinv, key=copyinv.get)
            values.append(copyinv[maximum])
            print(formatstr.format(copyinv[maximum], maximum))
            del copyinv[maximum]

    elif order == "count,asc":
        copyinv = dict(inventory)
        while len(copyinv) > 0:
            minimum = min(copyinv, key=copyinv.get)
            values.append(copyinv[minimum])
            print(formatstr.format(copyinv[minimum], minimum))
            del copyinv[minimum]

    print(2 * int(longest) * "-")
    print("Total number of items:", sum(values))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    file = open(filename, "r")
    cont = file.read()
    file.close()
    cont = cont.split(",")
    for i in cont:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    file = open(filename, "w")
    content = ""
    for i in inventory:
        content = content + (i + ",") * inventory[i]
    content = content[:-1]
    file.write(content)
    file.close()
