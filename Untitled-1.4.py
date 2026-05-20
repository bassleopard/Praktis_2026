def validate_brackets(code: str) -> bool:
    stack = []

    # Відповідність закриваючих дужок відкриваючим
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Перебір усіх символів у рядку
    for char in code:

        # Якщо відкриваюча дужка — додаємо у стек
        if char in "([{":
            stack.append(char)

        # Якщо закриваюча дужка — перевіряємо стек
        elif char in ")]}":

            # Якщо стек порожній — помилка
            if not stack:
                return False

            # Дістаємо останню відкриваючу дужку
            top = stack.pop()

            # Перевіряємо відповідність
            if pairs[char] != top:
                return False

    # Після перевірки стек має бути порожнім
    return len(stack) == 0