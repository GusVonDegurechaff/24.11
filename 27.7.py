def check_film_concept(durations):
    prev_duration = durations[0]
    for duration in durations[1:]:
        if duration != 2 * prev_duration:
            return "NO"
        prev_duration = duration
    return "YES"
durations = []
while True:
    duration = int(input("Введите длительность сцены (в минутах) или -1 для завершения: "))
    if duration == -1:
        break
    durations.append(duration)
result = check_film_concept(durations)
print(result)