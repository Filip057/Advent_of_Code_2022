def how_many_cal(input):
    final_list = []

    # loading data from txt to list
    with open(input, "r") as data:
        cal_list = data.readlines()

    space = ''
    # editing data
    for cal in cal_list:
        stripped = cal.strip("\n")
        if stripped != space:
            stripped = int(stripped)
        final_list.append(stripped)

    greatest_sum = 0
    second_greatest = 0
    thid_greatest = 0

    current_sum = 0
    for cal in final_list:
        if cal != space:
            current_sum += cal

        else:
            if current_sum > greatest_sum:
                thid_greatest = second_greatest
                second_greatest = greatest_sum
                greatest_sum = current_sum

            elif current_sum > second_greatest:
                thid_greatest = second_greatest
                second_greatest = current_sum

            elif current_sum > thid_greatest:
                thid_greatest = current_sum

            current_sum = 0

    top_three = [greatest_sum, second_greatest, thid_greatest]
    return sum(top_three)


print(how_many_cal("input.txt"))