#czy ja moge while zrobic
#czy ja moge uzywac metod dla list i str
import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_in = input("Enter new coordinates as floats in format 'x,y,z': ")
        list_pos = user_in.split(',')
        if len(list_pos) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(list_pos[0])
        except ValueError:
            print(f"Error on parameter {list_pos[0]}: could not convert string to float: {list_pos[0]}")
            continue
        try:
            y = float(list_pos[1])
        except ValueError:
            print(f"Error on parameter {list_pos[1]}: could not convert string to float: {list_pos[1]}")
            continue
        try:
            z = float(list_pos[2])
            break
        except ValueError:
            print(f"Error on parameter {list_pos[2]}: could not convert string to float: {list_pos[2]}")
            continue
    return x, y, z

def main():
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print("Get a second set of coordinates")
    pos2 = pos1 = get_player_pos()
    



if __name__ == "__main__":
    main()