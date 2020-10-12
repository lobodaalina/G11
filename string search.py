string = input("Пишите тут:")
a = input("Искомая буква:")
cnt = 0


def func(cnt):
    for i in string:
        if i == a:
            cnt = cnt + 1
    print("В строке буква", a, "встречается", cnt, "раз")


func(cnt)
