num=int(input("Введите число в диапозоне от 1 до 999: "))
if num%2 == 0:
    if num < 10:
        print("Четное число")
    elif num >= 10 and num < 100:
        print("Четное двузначное число")
    elif num >= 100 and num < 1000:
        print("Четное трехзначное число")
else:
    if num < 10:
        print("Нечетное число")
    elif num >= 10 and num < 100:
        print("Нечетное двузначное число")
    elif num >= 100 and num < 1000:
        print("Нечетное трехзначное число")