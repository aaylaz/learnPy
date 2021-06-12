

def lstrip(iterable, special_item):
    '''
    strips the beginning of an iterable if equal
    to defined item
    :param iterable: any iterable
    :param special_item: item to be stripped from the beginning
    :return: list of the iterable without the beginning
    '''

    iterable_list = list(iterable)
    if not iterable_list:
        yield iterable_list

    while iterable_list[0] == special_item:
        iterable_list.pop(0)
        if not iterable_list:
            return iterable_list

    return iterable_list

x = lstrip([], 1)

print(list(x))
print(list(x))

