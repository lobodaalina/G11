def merge(dict1, dict2):
    full_dict = dict1.copy()
    full_dict.update(dict2)
    return full_dict


def dict():
    a = input("Введите ключ 1:")
    b = input("Введите значение 1:")
    dict1 = {a: b}
    c = input("Введите ключ 2:")
    d = input("Введите значение 2:")
    dict2 = {c: d}
    print(merge(dict1, dict2))

dict()