

def with_previous(iterable, *, fillvalue=None):
    '''
    takes iterable and returns tuple of each item
    and previous item
    :param iterable: any iterable
    :return: iterable of tuples holding each item
    and the previous item
    '''
    if not iterable:
        return iterable

    first_value = fillvalue
    return_list = []
    for item in iterable:
        return_tuple = ((item, first_value))
        first_value = item
        yield(return_tuple)

print(list(with_previous([1, 2, 3], 0)))

