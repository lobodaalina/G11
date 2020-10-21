import math
def sec_to_time():
    sec = int(input("Введите количество секунд:"))
    minutes = sec / 60
    sec = sec % 60
    h = minutes / 60
    minutes = minutes % 60
    days = h / 24
    h = h % 24
    print(math.floor(days), "дней", math.floor(h), "часов", math.floor(minutes), "минут", math.floor(sec), "секунд")

sec_to_time()