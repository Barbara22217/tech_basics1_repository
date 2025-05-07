inventory = []
MAX_INVENTORY_SIZE = 5

items_in_room = [
    {"name": "Wood", "type": "material", "description": "Strong wood, perfect for a raft."},
    {"name": "Rope", "type": "material", "description": "Could be used to tie the raft."},
    {"name": "Water Bottle", "type": "drink", "description": "Essential for survival."},
    {"name": "Fish", "type": "food", "description": "Fresh fish to keep you fed."},
    {"name": "Banana", "type": "food", "description": "Tasty and full of energy."},
    {"name": "Torch", "type": "tool", "description": "Lights up dark places."}
]


def show_inventory():
    print("\nYour Inventory:")
    if not inventory:
        print("  (empty)")
    else:
        for item in inventory:
            print(f"- {item['name']} ({item['type']})")

def show_room_items():
    print("\nItems in the room:")
    if not items_in_room:
        print("  (nothing here)")
    else:
        for item in items_in_room:
            print(f"- {item['name']} ({item['type']})")

def pick_up(item_name):
    for item in items_in_room:
        if item["name"].lower() == item_name:
            if len(inventory) >= MAX_INVENTORY_SIZE:
                print(" Your inventory is full!")
                return
            inventory.append(item)
            items_in_room.remove(item)
            print(f" You picked up the {item['name']}.")
            check_escape_items()
            return
    print(" That item is not in the room.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name:
            inventory.remove(item)
            items_in_room.append(item)
            print(f" You dropped the {item['name']}.")
            return
    print(" That item is not in your inventory.")

def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name:
            if item["type"] in ["food", "drink"]:
                print(f" You used the {item['name']} to keep going.")
                inventory.remove(item)
            elif item["name"].lower() == "raft":
                # Placeholder: raft use not supported here
                print(" You can't use the raft here.")
            else:
                print(f" You used the {item['name']}.")
            return
    print(" That item is not in your inventory.")

def examine(item_name):
    for item in inventory + items_in_room:
        if item["name"].lower() == item_name:
            print(f" {item['name']}: {item['description']}")
            return
    print(" That item is not here.")

def check_escape_items():
    required = {"wood", "rope", "water bottle"}
    inventory_items = {item["name"].lower() for item in inventory}
    if required.issubset(inventory_items):
        print("\n You now have everything you need to build a raft!")
        print(" Congratulations! You've survived the island!")
        print(" Now you can escape!\n")
        exit()


def game_loop():
    print(" Welcome to Survive the Island!")
    print("Collect wood, rope, and a water bottle to escape.")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            pick_up(command[7:].strip())
        elif command.startswith("drop "):
            drop(command[5:].strip())
        elif command.startswith("use "):
            use(command[4:].strip())
        elif command.startswith("examine "):
            examine(command[8:].strip())
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print(" Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    game_loop()



