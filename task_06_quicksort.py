'''def quicksort(array):
    """Быстрая сортировка."""
    # Сохраняем длину массива в переменную.
    len_array = len(array)

    # Базовый случай рекурсии. Если длина массива меньше или равна 1,
    # то возвращаем этот массив, тем самым запуская обратный ход рекурсии.
    if len_array <= 1:
        return array
    # Определяем индекс опорного элемента и получаем сам опорный элемент:
    middle_element_index = len_array // 2
    pivot = array[middle_element_index]  # pivot - "ось, точка опоры".
    # Передаём в функцию partition() массив и опорный элемент;
    # partition() вернёт кортеж с тремя списками;
    # распаковываем этот кортеж в три переменные.
    left, center, right = partition(array, pivot)
    # Рекурсивно вызываем quicksort() для левого и правого списков,
    # а затем соединяем все три списка в один.
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    """
    Разбивает массив на три разных массива относительно опорного элемента.
    """
    # Создаём три пустых списка.
    left, center, right = [], [], []
    # Раскладываем элементы по спискам.
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    # Возвращаем кортеж с тремя списками.
    return left, center, right


arr = [44, 60, 10, 61, 60, 2, 62, 18, 2, 69]
result = quicksort(arr)
print(result)
'''


def quicksort(array):
    len_array = len(array)
    if len_array <= 1:
        return array
    middle_element_index = len_array // 2
    pivot = array[middle_element_index]
    left, center, right = partition(array, pivot)
    print(f'L{left} + C{center} + R{right}')
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    left, center, right = [], [], []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    return left, center, right


arr = [44, 60, 10, 61, 60, 2, 62, 18, 2, 69]
result = quicksort(arr)
print(result)
