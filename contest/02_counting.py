# def counting(staff: list[int], step):
#     index = 0
#     while len(staff) > 1:
#         index = (index + step - 1) % len(staff)
#         staff.pop(index)
#     return staff[0]


def counting(staff: list[int], step, index=0):
    if len(staff) == 1:
        return staff[0]
    index = (index + step - 1) % len(staff)
    staff.pop(index)
    return counting(staff, step, index)


if __name__ == '__main__':
    with open('input.txt', 'r') as file_inp:
        staff = list(range(1, int(file_inp.readline()) + 1))
        step = int(file_inp.readline())
    result = counting(staff, step)
    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
