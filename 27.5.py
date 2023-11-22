# Функция
def check_film_rule(z, sequence):
    frame_count = 0

    for element in sequence:
        if element == -1:
            # Проверяем условие для текущей сцены
            if frame_count % z != 0:
                return "NO"
            frame_count = 0
        else:
            frame_count += element

    return "YES"

# Ввод данных
z = int(input("Введите номер фильма: "))
sequence = []
element = 0

print("Введите последовательность (0 или 1), оканчивающуюся -1:")
while element != -1:
    element = int(input())
    sequence.append(element)

# Проверка правила
result = check_film_rule(z, sequence)
print(result)