def TrianglePS(a):
    P=3*a
    S=(a*a*((3)**0.5))/4
    return [P,S]
num = int(input("Введите длину треугольника: "))
print(*TrianglePS(num))