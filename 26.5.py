n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
k = int(input("Введите значение k: "))
b = int(input("Введите значение b: "))
def calculate_composers(n, m, k, b):
    for _ in range(n, m):
        k = (k + b) ** 2
    return int(k)
result = calculate_composers(n, m, k, b)
print(f"{result}")