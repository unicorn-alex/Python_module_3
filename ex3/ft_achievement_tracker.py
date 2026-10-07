import random

def gen_player_achievements() -> set[str]:

    achievements = ["Crafting Genius", "World Savior", "Master Explorer",
                    "Collector Supreme", "Untouchable", "Boss Slayer",
                    "Strategist", "Unstoppable", "Speed Runner", "Survivor",
                    "Treasure Hunter", "First Steps", "Sharp Mind",
                    "Boss Slayer", "Turd Burglar", "What Are You Doing",
                    "Unachievable"]

    player_achievements = set(random.sample(achievements, random.randint(5, 9)))
    return player_achievements

def main() -> None:
    print("=== Achievement Tracker System ===\n")
    
    player1 = gen_player_achievements()
    print(f"Player Alice: {player1}")

    player2 = gen_player_achievements()
    print(f"Player Bob: {player2}")

    player3 = gen_player_achievements()
    print(f"Player Charlie: {player3}")

    player4 = gen_player_achievements()
    print(f"Player Dylan: {player4}")

    print(f"\nAll distinct achievements: {player1.union(player2, player3, player4)}")

    print(f"\nCommon achievements: {player1.intersection(player2, player3, player4)}")

    print(f"\nOnly Alice has: {player1.difference(player2, player3, player4)}")
    print(f"Only Bob has: {player2.difference(player1, player3, player4)}")
    print(f"Only Charlie has: {player3.difference(player2, player1, player4)}")
    print(f"Only Dylan has: {player4.difference(player2, player3, player1)}")

    print(f"Alice is missing: ")
    print(f"Bob is missing: ")
    print(f"Charlie is missing: ")
    print(f"Dylan is missing: ")

if __name__ == "__main__":
    main()