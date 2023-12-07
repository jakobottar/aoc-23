from queue import Queue


def parse_line(line):
    _, winning, mine = get_decks(line)
    matches = len(winning & mine)

    if matches == 0:
        return 0
    return 2 ** (matches - 1)


def get_decks(line):
    # cut off card name
    card, line = line.split(":")
    winning, mine = line.split("|")

    card = int(card.split(" ")[-1])
    winning = set([int(x) for x in list(filter(lambda x: x.isdigit(), winning.split(" ")))])
    mine = set([int(x) for x in list(filter(lambda x: x.isdigit(), mine.split(" ")))])

    return card, winning, mine


def queue_of_cards(list_of_decks):
    q = Queue()
    for i in range(len(list_of_decks)):
        q.put(list_of_decks[i])

    counter = 0
    while not q.empty():
        counter += 1

        decks = q.get()
        num, winning, mine = decks

        matches = len(winning & mine)
        if matches == 0:
            continue
        for i in range(0, matches):
            q.put(list_of_decks[num + i])

    return counter


if __name__ == "__main__":
    FILENAME = "input.txt"
    # Part 1:
    with open(FILENAME, "r", encoding="utf-8") as f:
        scores = [parse_line(line.strip()) for line in f.readlines()]

    print(f"part 1: {sum(scores)}")

    # Part 2:
    with open(FILENAME, "r", encoding="utf-8") as f:
        decks = [get_decks(line.strip()) for line in f.readlines()]

    print(f"part 2: {queue_of_cards(decks)}")
