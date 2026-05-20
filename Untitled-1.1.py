def search_dictionary(dictionary: list, word: str) -> str:
    """
    Бінарний пошук слова у відсортованому електронному словнику.

    :param dictionary: відсортований список пар (word, definition)
    :param word: слово для пошуку
    :return: визначення слова або рядок "Слово не знайдено"

    Складність: O(log n)
    """

    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_word = dictionary[mid][0]

        if mid_word == word:
            return dictionary[mid][1]
        elif mid_word < word:
            left = mid + 1
        else:
            right = mid - 1

    return "Слово не знайдено"


if __name__ == '__main__':
    # Приклад відсортованого словника (за словом у лексикографічному порядку)
    sample_dict = [
        ("автомат", "Пристрій для автоматизованої роботи"),
        ("біг", "Фізична активність, що включає швидку ходу"),
        ("вікно", "Проріз у стіні для світла та повітря"),
        ("дом", "Житлове приміщення"),
        ("яблуко", "Солодкий плод дерева яблуні")
    ]

    # Демонстрація: шукаємо існуюче і неіснуюче слово
    tests = ["вікно", "кіт"]
    for t in tests:
        result = search_dictionary(sample_dict, t)
        print(f"Пошук '{t}': {result}")
