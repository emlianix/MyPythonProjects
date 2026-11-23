from decimal import Decimal


def fresco_goats(filename):
    possible_colours = []
    counts = {}
    section = None
    total = 0

    with open(filename, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line:
                continue

            if line == "COLOURS":
                section = "COLOURS"
                continue
            if line == "GOATS":
                section = "GOATS"
                continue

            if section == "COLOURS":
                possible_colours.append(line)
                counts[line] = 0
            elif section == "GOATS":
                if line in counts:
                    counts[line] += 1
                    total += 1

    threshold = Decimal("0.07")
    result = []

    if total > 0:
        total_dec = Decimal(total)
        for colour in possible_colours:
            if Decimal(counts[colour]) / total_dec > threshold:
                result.append(colour)

    result.sort()

    with open("answer.txt", "w", encoding="utf-8") as out_file:
        for colour in result:
            out_file.write(colour + "\n")