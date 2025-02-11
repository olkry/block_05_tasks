def template_sorting(arr_1: list[int], arr_2: list[int]):
    result_arr = []
    for num in arr_2:
        while num in arr_1:
            cross = arr_1.pop(arr_1.index(num))
            result_arr.append(cross)
    for i in range(1, len(arr_1)):
        current = arr_1[i]
        prev = i - 1
        while prev >= 0 and arr_1[prev] > current:
            arr_1[prev + 1] = arr_1[prev]
            prev -= 1
        arr_1[prev + 1] = current
    result_arr.extend(arr_1)
    return result_arr


if __name__ == '__main__':
    with open('input.txt', 'r') as file_inp:
        sort_num_1 = int(file_inp.readline())
        arr_1 = [int(n) for n in file_inp.readline().split()]
        sort_num_2 = int(file_inp.readline())
        arr_2 = [int(n) for n in file_inp.readline().split()]
    result = ' '.join(str(ch) for ch in template_sorting(arr_1, arr_2))
    with open('output.txt', 'w') as file_out:
        file_out.write(result)
