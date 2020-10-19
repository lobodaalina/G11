def func():
    n = int(input("Enter the number of elements:"))
    list = [i for i in range(n)]
    print(list)
    print("First number is", list[0])
    print("Last number is", list[-1])


func()