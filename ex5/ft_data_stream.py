import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["alice", "charlie", "bob", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release", "poop", "paint", "sing", "play a game", "scream"]
    while True:
        yield random.choice(names), random.choice(actions)


def consume_event(
    list_of_events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while list_of_events != []:
        event = random.choice(list_of_events)
        list_of_events.remove(event)
        yield event


def main() -> None:

    print("=== Game Data Stream Processor ===\n")

    events = gen_event()
    for i in range(1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_of_events: list[tuple[str, str]] = []
    for i in range(10):
        list_of_events.append(next(events))
    print(f"\nBuilt list of 10 events: {list_of_events}")

    for event in consume_event(list_of_events):
        print(f"\nGot event from list: {event}")
        print(f"Remains in list: {list_of_events}")


if __name__ == "__main__":
    main()
