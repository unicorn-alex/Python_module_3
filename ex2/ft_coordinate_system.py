import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_in = input("Enter new coordinates as floats in format 'x,y,z': ")
        list_pos = user_in.split(',')
        if len(list_pos) != 3:
            print("Invalid syntax")
            continue
        try:
            index = 0
            x = float(list_pos[index])
            index = 1
            y = float(list_pos[index])
            index = 2
            z = float(list_pos[index])
        except ValueError:
            print(f"Error on parameter {list_pos[index]}:",
                  f"could not convert string to float: {list_pos[index]}")
            continue
        else:
            break
    return x, y, z


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x1 = pos1[0]
    y1 = pos1[1]
    z1 = pos1[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_to_center = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Distance to center: {distance_to_center}")

    print("\nGet a second set of coordinates")
    pos2 = pos1 = get_player_pos()
    print(f"Got a second tuple: {pos2}")
    x2 = pos2[0]
    y2 = pos2[1]
    z2 = pos2[2]
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance_between = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_between}")


if __name__ == "__main__":
    main()
