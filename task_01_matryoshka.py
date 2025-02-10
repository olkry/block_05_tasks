import inspect


def print_call_stack():
    """Функция распечатки имён функций в стеке."""
    print([frame.function for frame in inspect.stack()])


class Matryoshka:

    def __init__(self, size, item=None):
        self.size = size
        self.inner_item = item


'''
# # Создаём самую маленькую матрёшку. Внутри неё ничего нет. Размер S.
# the_smallest_one = Matryoshka('S')

# # Создаём матрёшку побольше - размера M.
# # И передаём ей в конструктор самую маленькую матрёшку.
# the_middle_one = Matryoshka('M', the_smallest_one)

# # Создаём матрёшку побольше, размера L; передаём в её конструктор
# # матрёшку размера M.
# the_biggest_one = Matryoshka('L', the_middle_one)

# Можно без промежуточных элементов
the_biggest_one = Matryoshka('L', Matryoshka('M', Matryoshka('S')))

# Размер большой матрёшки.
print(the_biggest_one.size)

# Размер матрёшки, вложенной в большую.
print(the_biggest_one.inner_item.size)

# Размер матрёшки, вложенной во вложенную в большую.
print(the_biggest_one.inner_item.inner_item.size)

# Содержимое наименьшей матрёшки.
print(the_biggest_one.inner_item.inner_item.inner_item)
'''


def disassemble_matryoshka(matryoshka):
    """Функция разборки матрёшки."""
    print_call_stack()
    # Получаем вложенную матрёшку.
    inner_item = matryoshka.inner_item
    # Если вложенной матрёшки нет, значит, это была самая маленькая матрёшка
    # и работа закончена.
    if inner_item is None:
        print(
            'Все матрёшки разобраны! Размер последней '
            f'матрёшки: {matryoshka.size}')
        return
    # Если вложенная матрёшка есть, печатаем информационное сообщение...
    print(f'Разобрали матрёшку размера {matryoshka.size}, разбираем дальше!')
    # ...и рекурсивно вызываем ту же функцию,
    # но аргументом в неё передаём объект, вложенный в текущий:
    disassemble_matryoshka(inner_item)
    print_call_stack()


if __name__ == '__main__':
    print_call_stack()
    # Создаём экземпляр матрёшки из трёх фигурок.
    big_matryoshka = Matryoshka('L', Matryoshka('M', Matryoshka('S')))
    # Передаём эту матрёшку на разборку.
    disassemble_matryoshka(big_matryoshka)
    print_call_stack()
