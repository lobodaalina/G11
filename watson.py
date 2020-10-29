def func():
    a = int(input("Enter your number:"))
    f1 = a % 10
    a = a // 10
    f2 = a % 10
    a = a // 10
    f3 = a % 10
    print(f1 + f2 + f3)


func()
