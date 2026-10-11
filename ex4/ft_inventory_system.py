import sys

def fill_inventory(args : list[str]) -> dict[str, int]:
    inventory = {}
    for arg in args:
        key_and_value = arg.split(":")
        if len(key_and_value) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key = key_and_value[0]
        if key in inventory.keys():
            print(f"Redundant item {key} - discarding")
            continue
        try:
            value = int(key_and_value[1])
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
        else:
            inventory.update({key: value})
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===\n")

    inventory = fill_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}\n")

    items = list(inventory.keys())
    print(f"Item list: {items}\n")
    
    total_items = sum(inventory.values())
    print(f"Total quality of the {len(items)} items: {total_items}\n")

    i = 0
    for item in inventory:
        print(f"Item {item} represents {round(inventory[item] / total_items * 100, 1)}%")
        if 
    

    



if __name__ == "__main__":
    main()