class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def is_palindrome(phrase: str) -> bool:
    # залишаємо лише літери та цифри, приводимо до нижнього регістру
    cleaned = []
    for ch in phrase:
        if ch.isalnum():
            cleaned.append(ch.lower())

    dq = Deque()

    # заповнюємо дек
    for ch in cleaned:
        dq.add_rear(ch)

    # порівнюємо символи з обох кінців
    while len(dq.items) > 1:
        front = dq.remove_front()
        rear = dq.remove_rear()
        if front != rear:
            return False

    return True


# Приклади використання
if __name__ == "__main__":
    tests = [
        "A man, a plan, a canal, Panama",
        "No lemon, no melon",
        "Hello, world",
        "Madam",
        "Was it a car or a cat I saw?"
    ]

    for t in tests:
        print(f"{t} -> {is_palindrome(t)}")