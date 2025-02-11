def fibon_bar(generate, first=0, second=1):
    res = first + second
    if generate <= 2:
        print(res)
        return
    fibon_bar(generate - 1, second, res)


def fib_recurs(generate):
    if generate <= 1:
        return generate
    else:
        return fib_recurs(generate - 1) + fib_recurs(generate - 2)


def fib_iter(generate):
    a, b = 0, 1
    for _ in range(generate):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    version = int(input())
    fibon_bar(version)
    print(fib_recurs(version))
    print(fib_iter(version))
    # with open('input.txt', 'r') as file_inp:
    #     version = file_inp.readline()
    # result = fibon_bar(6)
    # print(result)
    # with open('output.txt', 'w') as file_out:
    #     file_out.write(str(result))
