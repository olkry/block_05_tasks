def block_split(arr: list[int], count):
    result = 0
    max_val = 0
    for i in range(count):
        max_val = max(max_val, arr[i])
        if max_val == i:
            result += 1
    return result


if __name__ == '__main__':
    with open('contest/input.txt', 'r') as file_inp:
        count_num = int(file_inp.readline())
        numbers = [int(ch) for ch in file_inp.readline().split()]
    result = block_split(numbers, count_num)
    with open('contest/output.txt', 'w') as file_out:
        file_out.write(str(result))
