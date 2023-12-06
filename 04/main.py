

def parse_line(line):

    # cut off card name
    line = line.split(":")[1]
    winning, mine = line.split("|")

    winning = set([int(x) for x in list(filter(lambda x: x.isdigit(), winning.split(" ")))])
    mine = set([int(x) for x in list(filter(lambda x: x.isdigit(), mine.split(" ")))])

    matches = len(winning & mine)

    if matches == 0:
        return 0
    return 2 ** (matches - 1)


if __name__ == "__main__":
    FILENAME = "example.txt"
    # Part 1:
    with open(FILENAME, "r", encoding="utf-8") as f:
        scores = [parse_line(line.strip()) for line in f.readlines()]
    
    print(f"part 1: {sum(scores)}")
