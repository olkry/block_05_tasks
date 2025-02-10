def stairs_builder(n):
    if n == 0:  # Базовый случай.
        print('Испанская лестница построена!')
        return
    """Построить 1 ступеньку."""
    print(f'Осталось построить ступеней: {n}.')
    stairs_builder(n - 1)


# def pluser(num):
#     num += 5
#     if num > 100:
#         print(num, 'STOP')
#         return
#     print("Last", num)

#     pluser(num)


# Вызываем функцию, планируем построить лестницу из 138 ступенек.
stairs_builder(138)
# print(pluser(32))
