import sys


def validation_index(i, l_):
    if 0 <= i < len(l_):
        return True
    return False


def min_max_even_odd(m_c, s_c, list_):
    result = None
    if m_c == 'max' and s_c == 'even':
        searched_index = None
        max_number = - sys.maxsize
        for i,x in enumerate(list_):
            if x % 2 == 0:
                if x >= max_number:
                    max_number = x
                    searched_index = i
        if searched_index != None:
            result = searched_index
        else:
            result = 'No matches'
    elif m_c == 'max' and s_c == 'odd':
        searched_index = None
        max_number = - sys.maxsize
        for i, x in enumerate(list_):
            if x % 2 != 0:
                if x >= max_number:
                    max_number = x
                    searched_index = i
        if searched_index != None:
            result = searched_index
        else:
            result = 'No matches'
    elif m_c == 'min' and s_c == 'even':
        searched_index = None
        min_number = sys.maxsize
        for i,x in enumerate(list_):
            if x % 2 == 0:
                if x <= min_number:
                    min_number = x
                    searched_index = i
        if searched_index != None:
            result = searched_index
        else:
            result = 'No matches'
    elif m_c == 'min' and s_c == 'odd':
        searched_index = None
        min_number = sys.maxsize
        for i, x in enumerate(list_):
            if x % 2 != 0:
                if x <= min_number:
                    min_number = x
                    searched_index = i
        if searched_index != None:
            result = searched_index
        else:
            result = 'No matches'
    return result


def digits_counter(m_c, t_d, c, l_):
    result = None
    if m_c == 'first' and t_d == 'even':
        if c > len(l_):
            result = 'Invalid count'
            return result
        list_result = []
        for num in l_:
            if num % 2 == 0 and c > 0:
                c -= 1
                list_result.append(num)
        result = list_result
    elif m_c == 'first' and t_d == 'odd':
        if c > len(l_):
            result = 'Invalid count'
            return result
        list_result = []
        for num in l_:
            if num % 2 != 0 and c > 0:
                c -= 1
                list_result.append(num)
        result = list_result
    elif m_c == 'last' and t_d == 'even':
        if c > len(l_):
            result = 'Invalid count'
            return result
        list_result = []
        for num in l_:
            if num % 2 == 0:
                list_result.append(num)
        list_result = list_result[-c:]
        result = list_result
    elif m_c == 'last' and t_d == 'odd':
        if c > len(l_):
            result = 'Invalid count'
            return result
        list_result = []
        for num in l_:
            if num % 2 != 0:
                list_result.append(num)
        list_result = list_result[-c:]
        result = list_result
    return result


list_ = [int(x) for x in input().split()]

command = input()
while command != 'end':
    command_args = command.split()
    main_command = command_args[0]
    if main_command == 'exchange':
        index = int(command_args[1])
        if validation_index(index, list_):
            first_segment = list_[:index + 1]
            second_segment = list_[index + 1:]
            list_ = second_segment + first_segment
        else:
            print('Invalid index')
    elif main_command == 'max':
        subcommand = command_args[1]
        result = min_max_even_odd(main_command, subcommand,list_)
        print(result)
    elif main_command == 'min':
        subcommand = command_args[1]
        result = min_max_even_odd(main_command, subcommand, list_)
        print(result)
    elif main_command == 'first':
        count = int(command_args[1])
        type_digits = command_args[2]
        result = digits_counter(main_command, type_digits, count, list_)
        print(result)
    elif main_command == 'last':
        count = int(command_args[1])
        type_digits = command_args[2]
        result = digits_counter(main_command, type_digits, count, list_)
        print(result)
    command = input()
print(list_)
