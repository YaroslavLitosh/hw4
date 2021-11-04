from const import numbers, result_list


def get_denominator(file_name):
    try:
        handle = open(file_name, "r")
        global denominator
        denominator = int(handle.read())
        handle.close()
    except FileNotFoundError:
        print('File not found!')
    except ValueError:
        print('Please, enter number!')
    return denominator


def get_list_of_numbers(denominator):
    try:
        for item in numbers:
            if item % int(denominator) == 0:
                result_list.append(item)
    except ZeroDivisionError:
        print('Enter not zero number')


def get_sum(result_list):
    global result
    result = 0
    for item in result_list:
        result += item
    return result


def write_result (result, name_of_result_file):
    file = open(name_of_result_file, 'w')
    file.write(f'Your sum is {result}')


def start():
    get_denominator('d.txt')
    get_list_of_numbers(denominator)
    get_sum(result_list)
    write_result(result, 'result_file')


