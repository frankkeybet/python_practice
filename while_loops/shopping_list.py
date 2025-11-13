shopping_list = ["Bread", "Milk", "Eggs", "Butter"]
item_found = False

while not item_found:
    item = input("Search for an item in the shopping list (or 'q' to quit): ")
    if item.lower() == 'q':
        break  # Exit the loop if user enters 'q'
    if item in shopping_list:
        item_found = True
        print(f"{item} is available in the shopping list.")
    else:
        print(f"{item} is not in the shopping list. Please try again.")
    