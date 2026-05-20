def create_rating(students: list) -> list:
    """
    Формує рейтинг студентів за середнім балом (спаданням)
    за допомогою алгоритму Selection Sort.

    :param students: список кортежів (ім'я, середній бал)
    :return: відсортований список (від найвищого балу до найнижчого)
    """

    n = len(students)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if students[j][1] > students[max_index][1]:
                max_index = j

        # обмін елементів
        students[i], students[max_index] = students[max_index], students[i]

    return students


# Приклад вхідних даних
students = [
    ("Олена", 87),
    ("Іван", 92),
    ("Марія", 92),
    ("Петро", 75),
    ("Андрій", 81)
]

# Формування рейтингу
rating = create_rating(students)

# Виведення результату
for name, score in rating:
    print(f"{name}: {score}")