num_students = int(input("Введите количество студентов: "))
students_data = []
for _ in range(num_students):
    first_name = input("Введите имя студента: ")
    middle_name = input("Введите отчество студента: ")
    last_name = input("Введите фамилию студента: ")
    grades = int(input(f"Введите количество оценок для {first_name} {last_name}: "))
    summ = 0
    for i in range(1, grades + 1):
        g = int(input(f"Введите {i}-е число: "))
        summ += g
    average = summ / grades
    students_data.append((last_name, first_name, middle_name, average))
print("\nСредние баллы всех студентов:")
for student in students_data:
    last_name, first_name, middle_name, average = student
    print(f"{last_name} {first_name} {middle_name}: {average:.2f}")