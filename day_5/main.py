"""
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9 
 """

import re

with open("orders.txt", "r") as data:
    orders = [line.rstrip('\n') for line in data]


def move_item(number, origin, to):
    how_many = number
    while how_many > 0:
        n = origin.pop()
        to.append(n)
        how_many -= 1


stacks = {
    1: ["W", "B", "D", "N", "C", "F", "J"],
    2: ["P", "Z", "V", "Q", "L", "S", "T"],
    3: ["P", "Z", "B", "G", "J", "T"],
    4: ["G", "T", "L", "J", "Z", "B", "H", "C"],
    5: ["G", "V", "B", "J", "S"],
    6: ["P", "S", "Q"],
    7: ["B", "V", "D", "F", "L", "M", "P", "N"],
    8: ["P", "S", "M", "F", "B", "D", "L", "R"],
    9: ["V", "D", "T", "R"]
}

"""
for step in orders:
    instruction = re.findall(r'\d+', step)
    move = int(instruction[0])
    from_loc = int(instruction[1])
    to_loc = int(instruction[2])
    move_item(number=move, origin=stacks[from_loc], to=stacks[to_loc])

final_1 = ""
for i in range(1, 10):
    index = len(stacks[i]) - 1
    last_item = stacks[i][index]
    final_1 += last_item


print(final_1)
"""


