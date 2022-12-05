with open("IDnumbers.txt", "r") as data:
    idNumbers = [line.rstrip('\n').split(",") for line in data]


def part_one(idnums):
    nums_of_fullyContains = 0
    for section in idnums:
        first_interval = set([i for i in range(int(section[0].split("-")[0]), int(section[0].split("-")[1]) + 1)])
        second_interval = set([i for i in range(int(section[1].split("-")[0]), int(section[1].split("-")[1]) + 1)])

        if first_interval.issubset(second_interval) or second_interval.issubset(first_interval):
            nums_of_fullyContains += 1

    return f"this is solution to part_1 {nums_of_fullyContains}"


def part_two(idnums):
    nums_of_fullyContains = 0
    for section in idnums:
        first_interval = set([i for i in range(int(section[0].split("-")[0]), int(section[0].split("-")[1]) + 1)])
        second_interval = set([i for i in range(int(section[1].split("-")[0]), int(section[1].split("-")[1]) + 1)])

        if len(first_interval.intersection(second_interval)) >= 1:
            nums_of_fullyContains += 1

    return f"this is solution to part_2 {nums_of_fullyContains}"


print(part_one(idNumbers))
print(part_two(idNumbers))
