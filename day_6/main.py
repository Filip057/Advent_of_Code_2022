
with open("signal.txt", "r") as data:
    signal = [line.rstrip('\n') for line in data]


def find_marker(data):
    total_score = 0

    for line in data:
        for i in range(len(line)):
            marker = line[i:i+14]
            marker_list = [ch for ch in marker]
            if len(set(marker_list)) == 14:
                total_score += i+14
                break

    return total_score


print(find_marker(signal))
