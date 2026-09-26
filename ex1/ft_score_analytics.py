import sys


def create_scores(args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in args:
        try:
            nb = int(arg)
        except ValueError:
            print(f"Invalid parameter: {arg}")
        else:
            scores += [nb]
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = create_scores(sys.argv[1:])
    nb_of_scores = len(scores)
    if nb_of_scores == 0:
        print("No scores provided. Usage: python3",
              "ft_score_analytics.py <score1> <score2> ...")
        return

    max_score = max(scores)
    min_score = min(scores)
    print(f"Total players {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / nb_of_scores}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    main()
