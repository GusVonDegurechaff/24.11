n = int(input("Введите количество фильмов: "))
total_duration = 0
for i in range(n):
    duration = int(input(f"Введите длительность фильма {i+1} : "))
    total_duration += duration
print(f"Общая длительность фильмов: {total_duration} часов")