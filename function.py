a = int(input("Enter number:"))
b = int(input("Enter number:"))


def myfunc(a, b):
    if a > b:
        print("Все будет хорошо")
    elif a < b:
        print("Пошел отсюда быстро")
    else:
        print("Скоро рассвет, выхода нет")


myfunc(a, b)
