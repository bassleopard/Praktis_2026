def search_dictionary(dictionary: list, word: str) -> str:
    """
    Виконує бінарний пошук слова у відсортованому словнику.

    :param dictionary: відсортований список пар (слово, визначення)
    :param word: слово для пошуку
    :return: визначення слова або повідомлення про відсутність
    """

    left = 0
    right = len(dictionary) - 1

    while left <= right:
        middle = (left + right) // 2

        current_word = dictionary[middle][0]
        current_definition = dictionary[middle][1]

        if current_word == word:
            return current_definition

        elif current_word < word:
            left = middle + 1

        else:
            right = middle - 1

    return "Слово не знайдено"


# Відсортований електронний словник
dictionary = [
    ("Алгоритм", "Послідовність дій для розв'язання задачі"),
    ("База даних", "Організована сукупність даних"),
    ("Клас", "Шаблон для створення об'єктів"),
    ("Масив", "Структура даних для зберігання елементів"),
    ("Функція", "Іменований блок коду")
]

# Введення слова для пошуку
word = input("Введіть слово: ")

# Пошук слова
result = search_dictionary(dictionary, word)

# Виведення результату
print(result)