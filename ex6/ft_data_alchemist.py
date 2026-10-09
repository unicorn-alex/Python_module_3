import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    all_players_capitalized = [
        player.capitalize() for player in players]
    print(f"New list with all names capitalized: {all_players_capitalized}")

    only_capitalized_players = [
        player for player in players if player == player.capitalize()]
    print(f"New list of capitalized names only: {only_capitalized_players}\n")

    scores = {
        player: random.randint(0, 1000) for player in all_players_capitalized}
    print(f"Score dict: {scores}")

    average = round(sum(scores.values()) / len(scores.values()), 2)
    print(f"Score average: {average}")

    high_scores = {
        player: score for player, score in scores.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
