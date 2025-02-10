def fibon_bar(generate, first=0, second=1):
    res = first + second
    if generate <= 1:
        print(res)
        return
    fibon_bar(generate - 1, second, res)


if __name__ == '__main__':
    version = int(input())
    fibon_bar(version)
    # with open('input.txt', 'r') as file_inp:
    #     version = file_inp.readline()
    # result = fibon_bar(6)
    # print(result)
    # with open('output.txt', 'w') as file_out:
    #     file_out.write(str(result))
