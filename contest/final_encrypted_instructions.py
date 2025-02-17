#  133560522

def encrypted_instructions(instruction: str) -> str:
    '''
    Функция декодирующая команды для марсохода.

    Аргументы:
    instruction (str): Строка, содержащая вложенные команды с количеством
    повторов в виде чисел.

    Возвращает:
    str: Последовательную строку с командами.
    '''
    command_stack: list[tuple[int, str]] = list()
    repeat_count: str = ''
    result: str = ''

    for char in instruction:
        if char.isalpha():
            result += char
        elif char.isdigit():
            repeat_count += char
        elif char == '[':
            command_stack.append((int(repeat_count), result))
            repeat_count = ''
            result = ''
        else:
            count, previous_command = command_stack.pop()
            result = previous_command + result * count
    return result


if __name__ == '__main__':
    with open('contest/input.txt', 'r') as file_in:
        from_home_instruction = file_in.readline().strip()
    result = encrypted_instructions(from_home_instruction)
    with open('contest/output.txt', 'w') as file_out:
        file_out.write(result)
