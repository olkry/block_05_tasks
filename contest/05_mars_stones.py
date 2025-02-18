def deliver_for_museum(arr1: list[int], arr2: list[int]):
    arr1.sort()
    arr2.sort()
    orders, delivery = 0, 0
    count = 0
    while orders < len(arr1) and delivery < len(arr2):
        if arr1[orders] <= arr2[delivery]:
            count += 1
            orders += 1
        delivery += 1
    return count


if __name__ == '__main__':
    with open('contest/input.txt', 'r') as in_file:
        order = in_file.readline()
        order_list = [int(num) for num in in_file.readline().split()]
        income = in_file.readline()
        income_list = [int(num) for num in in_file.readline().split()]
    result = deliver_for_museum(order_list, income_list)
    with open('contest/output.txt', 'w') as out_file:
        out_file.write(str(result))
