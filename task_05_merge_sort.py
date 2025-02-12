'''
def merge(left, right):
    # Создаём пустой список result.
    # Сразу создать результирующий список нужной длины не получится:
    # элементы будут добавляться в конец списка,
    # а не занимать места по индексам.
    result = []

    # Удалять элементы из массивов невыгодно: возрастёт временная сложность.
    # Вместо этого будем двигать по массивам указатели.
    # Устанавливаем их на стартовую позицию:
    left_idx, right_idx = 0, 0

    # Сохраняем длины массивов, чтобы не считать их на каждом шаге цикла.
    len_left, len_right = len(left), len(right)

    # Пока ни один указатель не дошёл до конца своего массива...
    while left_idx < len_left and right_idx < len_right:
        # ...сравниваем элементы, на которые "смотрят" указатели.
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            # Если перенесли элемент из left,
            # увеличиваем значение указателя left_idx.
            left_idx += 1
        else:
            result.append(right[right_idx])
            # Если перенесли элемент из right,
            # увеличиваем значение указателя right_idx.
            right_idx += 1

    # Добавляем в result оставшиеся элементы,
    # когда один массив закончился, а второй нет.
    return result + left[left_idx:] + right[right_idx:]
'''


def merge_sort(array):
    # Сохраняем длину массива в переменную, чтобы не считать её каждый раз.
    len_array = len(array)
    # Базовый случай рекурсии.
    if len_array <= 1:
        return array

    # Рекурсивный разбор массива в левой половине:
    # передаём в merge_sort() левую половину полученного на вход массива.
    left = merge_sort(array[0: len_array // 2])

    # Рекурсивный разбор массива в правой половине:
    # передаём в merge_sort() правую половину полученного на вход массива.
    right = merge_sort(array[len_array // 2: len_array])

    return merge(left, right)


# А функция сортировки и слияния у нас уже есть!
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    len_left, len_right = len(left), len(right)

    while left_idx < len_left and right_idx < len_right:
        # Сравниваем:
        if left[left_idx] <= right[right_idx]:
            # Добавляем в result:
            result.append(left[left_idx])
            # Сдвигаем указатель:
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]


test_array = [5, 4, 9, 10, 8, 3, 11, 1, 7, 6, 2]
print(merge_sort(test_array))
